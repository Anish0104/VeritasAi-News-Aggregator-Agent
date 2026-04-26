from __future__ import annotations

import json
import textwrap
import uuid
from pathlib import Path


NOTEBOOK_NAME = "VeritasAI_Colab_Submission.ipynb"


def md(source: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {"id": uuid.uuid4().hex[:8]},
        "source": textwrap.dedent(source).strip("\n") + "\n",
    }


def code(source: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {"id": uuid.uuid4().hex[:8]},
        "outputs": [],
        "source": textwrap.dedent(source).rstrip() + "\n",
    }


FETCH_NEWS = textwrap.dedent(
    r'''
    from __future__ import annotations

    import html
    import re
    import time
    from urllib.error import HTTPError, URLError
    from urllib.parse import quote_plus
    from urllib.request import Request, urlopen

    import feedparser


    GOOGLE_NEWS_TEMPLATE = (
        "https://news.google.com/rss/search?q={query}&hl={hl}&gl={gl}&ceid={ceid}"
    )
    DEFAULT_HEADERS = {
        "User-Agent": "Mozilla/5.0 (compatible; VeritasAI/1.0; +https://news.google.com)"
    }


    def build_google_news_url(query: str, language: str = "en-US", country: str = "US") -> str:
        safe_query = quote_plus((query or "").strip())
        return GOOGLE_NEWS_TEMPLATE.format(
            query=safe_query,
            hl=language,
            gl=country,
            ceid=f"{country}:en",
        )


    def normalize_whitespace(value: str) -> str:
        return re.sub(r"\s+", " ", (value or "")).strip()


    def strip_tags(value: str) -> str:
        return normalize_whitespace(re.sub(r"<[^>]+>", " ", html.unescape(value or "")))


    def download_feed(url: str, attempts: int = 2, timeout: int = 8) -> bytes:
        for attempt in range(attempts):
            try:
                request = Request(url, headers=DEFAULT_HEADERS)
                with urlopen(request, timeout=timeout) as response:
                    return response.read()
            except (HTTPError, URLError, TimeoutError, OSError):
                if attempt + 1 < attempts:
                    time.sleep(0.6)
        return b""


    def entry_get(entry, key: str, default=None):
        if hasattr(entry, "get"):
            try:
                return entry.get(key, default)
            except Exception:
                pass
        return getattr(entry, key, default)


    def split_headline_source(title: str) -> tuple[str, str]:
        clean_title = normalize_whitespace(html.unescape(title))
        if " - " in clean_title:
            headline, source = clean_title.rsplit(" - ", 1)
            if 1 <= len(source.split()) <= 6:
                return headline.strip(), source.strip()
        return clean_title, "Unknown Source"


    def article_from_entry(entry, topic: str, query: str) -> dict:
        raw_title = getattr(entry, "title", "") or ""
        headline, fallback_source = split_headline_source(raw_title)
        source = fallback_source
        entry_source = getattr(entry, "source", None)
        if entry_source and getattr(entry_source, "title", None):
            source = normalize_whitespace(entry_source.title)
        raw_summary = (
            entry_get(entry_get(entry, "summary_detail", {}), "value", "")
            or getattr(entry, "summary", "")
            or ""
        )

        return {
            "topic": topic,
            "query": query,
            "headline": headline,
            "translated_headline": headline,
            "link": getattr(entry, "link", "") or "",
            "source": source or "Unknown Source",
            "published": getattr(entry, "published", "")
            or getattr(entry, "updated", "")
            or "",
            "raw_title": raw_title,
            "summary": strip_tags(raw_summary),
        }


    def fetch_news(
        topic: str,
        max_articles: int = 15,
        language: str = "en-US",
        country: str = "US",
        display_topic: str | None = None,
    ) -> list[dict]:
        topic = (topic or "").strip()
        display_topic = (display_topic or topic).strip()
        if not topic:
            return []

        url = build_google_news_url(topic, language=language, country=country)
        feed_bytes = download_feed(url)
        if not feed_bytes:
            return []

        parsed = feedparser.parse(feed_bytes)
        entries = getattr(parsed, "entries", []) or []
        articles = []

        for entry in entries[: max_articles or 15]:
            try:
                article = article_from_entry(entry, topic=display_topic, query=topic)
                if article["headline"] and article["link"]:
                    articles.append(article)
            except Exception:
                continue

        return articles


    def fetch_all_topics(topics: list[str], max_articles: int = 15) -> list[dict]:
        all_articles = []
        for topic in topics or []:
            all_articles.extend(fetch_news(topic, max_articles=max_articles, display_topic=topic))
        return all_articles
    '''
).strip("\n")


SENTIMENT = textwrap.dedent(
    r'''
    from __future__ import annotations

    from collections import defaultdict
    from datetime import datetime, timezone
    from typing import Iterable

    from dateutil import parser as date_parser
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


    analyzer = SentimentIntensityAnalyzer()
    SENTIMENT_LABELS = ("Positive", "Negative", "Neutral")


    def parse_date(date_string: str) -> dict:
        if not date_string:
            parsed = datetime.now(timezone.utc)
        else:
            try:
                parsed = date_parser.parse(date_string)
            except Exception:
                parsed = datetime.now(timezone.utc)

        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)

        parsed = parsed.astimezone(timezone.utc)
        return {
            "published_iso": parsed.isoformat(),
            "published_display": parsed.strftime("%b %d, %Y %H:%M UTC"),
            "timestamp": parsed.timestamp(),
        }


    def get_sentiment(headline: str) -> tuple[str, float]:
        score = analyzer.polarity_scores((headline or "").strip()).get("compound", 0.0)
        if score >= 0.05:
            label = "Positive"
        elif score <= -0.05:
            label = "Negative"
        else:
            label = "Neutral"
        return label, round(float(score), 3)


    def _dedupe_key(article: dict) -> tuple[str, str, str]:
        return (
            (article.get("topic") or "").strip().lower(),
            (article.get("link") or "").strip().lower(),
            (article.get("headline") or "").strip().lower(),
        )


    def process_articles(articles: Iterable[dict], limit_per_topic: int = 10) -> list[dict]:
        unique_articles: dict[tuple[str, str, str], dict] = {}

        for article in articles or []:
            enriched = dict(article)
            enriched.setdefault("translated_headline", enriched.get("headline", ""))
            enriched.update(parse_date(enriched.get("published", "")))
            sentiment, score = get_sentiment(enriched.get("headline", ""))
            enriched["sentiment"] = sentiment
            enriched["sentiment_score"] = score

            key = _dedupe_key(enriched)
            existing = unique_articles.get(key)
            if existing is None or enriched["timestamp"] > existing["timestamp"]:
                unique_articles[key] = enriched

        grouped: dict[str, list[dict]] = defaultdict(list)
        for article in unique_articles.values():
            grouped[article.get("topic") or "General"].append(article)

        trimmed_articles: list[dict] = []
        for group in grouped.values():
            group.sort(key=lambda item: item["timestamp"], reverse=True)
            trimmed_articles.extend(group[:limit_per_topic])

        trimmed_articles.sort(key=lambda item: item["timestamp"], reverse=True)
        return trimmed_articles


    def sentiment_breakdown(articles: Iterable[dict]) -> dict:
        counts = {label: 0 for label in SENTIMENT_LABELS}
        article_list = list(articles or [])

        for article in article_list:
            label = article.get("sentiment", "Neutral")
            if label not in counts:
                label = "Neutral"
            counts[label] += 1

        total = len(article_list)
        percentages = {
            label: round((count / total) * 100, 1) if total else 0.0
            for label, count in counts.items()
        }

        return {
            "total": total,
            "counts": counts,
            "percentages": percentages,
        }
    '''
).strip("\n")


NLP_PIPELINE = textwrap.dedent(
    r'''
    from __future__ import annotations

    from collections import Counter
    from functools import lru_cache

    import spacy
    from sumy.nlp.tokenizers import Tokenizer
    from sumy.parsers.plaintext import PlaintextParser
    from sumy.summarizers.text_rank import TextRankSummarizer


    ALLOWED_ENTITY_LABELS = {
        "PERSON",
        "ORG",
        "GPE",
        "LOC",
        "PRODUCT",
        "EVENT",
        "NORP",
        "WORK_OF_ART",
    }

    VAGUE_TOPICS = {
        "ai",
        "news",
        "technology",
        "economy",
        "markets",
        "business",
        "politics",
        "science",
        "weather",
        "sports",
        "war",
        "finance",
        "energy",
        "trade",
    }


    @lru_cache(maxsize=1)
    def get_nlp():
        return spacy.load("en_core_web_sm")


    def extract_entities_from_query(query: str) -> list[str]:
        query = (query or "").strip()
        if not query:
            return []

        doc = get_nlp()(query)
        entities = []
        seen = set()

        for ent in doc.ents:
            cleaned = ent.text.strip()
            if cleaned and cleaned.lower() not in seen:
                seen.add(cleaned.lower())
                entities.append(cleaned)

        return entities


    def extract_keywords(articles: list[dict], top_n: int = 15) -> list[dict]:
        text = " ".join(article.get("headline", "") for article in articles or [])
        if not text.strip():
            return []

        doc = get_nlp()(text)
        counter = Counter()

        for token in doc:
            if token.is_stop or token.is_punct or token.is_space or token.like_num:
                continue
            if token.pos_ not in {"NOUN", "PROPN", "ADJ"}:
                continue
            cleaned = token.lemma_.strip().lower()
            if len(cleaned) < 3:
                continue
            counter[cleaned] += 1

        return [
            {"term": term, "count": count}
            for term, count in counter.most_common(top_n)
        ]


    def generate_briefing(articles: list[dict], sentence_count: int = 3) -> str:
        if not articles:
            return "No live articles were available yet, so the briefing will appear after the first successful fetch."

        headline_text = ". ".join(article.get("headline", "") for article in articles if article.get("headline"))
        if headline_text.count(".") < 2:
            fallback = [article.get("headline", "") for article in articles[:3]]
            return " ".join(part for part in fallback if part).strip()

        try:
            parser = PlaintextParser.from_string(headline_text, Tokenizer("english"))
            summarizer = TextRankSummarizer()
            summary = summarizer(parser.document, sentence_count)
            rendered = " ".join(str(sentence) for sentence in summary).strip()
            if rendered:
                return rendered
        except Exception:
            pass

        fallback = [article.get("headline", "") for article in articles[:3]]
        return " ".join(part for part in fallback if part).strip()


    def extract_followup_suggestions(
        articles: list[dict],
        topic: str,
        limit: int = 3,
    ) -> list[str]:
        combined_text = " ".join(article.get("headline", "") for article in articles or [])
        if not combined_text.strip():
            return []

        doc = get_nlp()(combined_text)
        suggestions = []
        seen = {(topic or "").strip().lower()}

        for ent in doc.ents:
            cleaned = ent.text.strip()
            lowered = cleaned.lower()
            if not cleaned or ent.label_ not in ALLOWED_ENTITY_LABELS:
                continue
            if lowered in seen or len(cleaned) < 3:
                continue
            suggestions.append(cleaned)
            seen.add(lowered)
            if len(suggestions) >= limit:
                return suggestions

        for keyword in extract_keywords(articles, top_n=10):
            term = keyword["term"].replace("_", " ").title()
            lowered = term.lower()
            if lowered in seen:
                continue
            suggestions.append(term)
            seen.add(lowered)
            if len(suggestions) >= limit:
                break

        return suggestions[:limit]


    def assess_topic_specificity(topic: str) -> str:
        topic = (topic or "").strip()
        if not topic:
            return "vague"

        doc = get_nlp()(topic)
        entity_labels = {ent.label_ for ent in doc.ents}
        lowered = topic.lower()

        if "PERSON" in entity_labels:
            return "person"
        if entity_labels & {"ORG", "PRODUCT", "GPE", "LOC", "EVENT", "NORP"}:
            return "specific"
        if len(topic.split()) >= 2:
            return "specific"
        if lowered in VAGUE_TOPICS:
            return "vague"

        token_count = sum(1 for token in doc if not token.is_space and not token.is_punct)
        if token_count <= 1:
            return "vague"
        return "specific"
    '''
).strip("\n")


TRANSLATOR = textwrap.dedent(
    r'''
    from __future__ import annotations

    from functools import lru_cache

    from transformers import MarianMTModel, MarianTokenizer


    LANGUAGE_CONFIG = {
        "English": None,
        "Spanish": "Helsinki-NLP/opus-mt-en-es",
        "Hindi": "Helsinki-NLP/opus-mt-en-hi",
        "French": "Helsinki-NLP/opus-mt-en-fr",
        "German": "Helsinki-NLP/opus-mt-en-de",
    }


    @lru_cache(maxsize=4)
    def load_translator(language: str):
        model_name = LANGUAGE_CONFIG.get(language)
        if not model_name:
            return None, None

        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        return tokenizer, model


    def translate_headline(headline: str, language: str) -> str:
        if language not in LANGUAGE_CONFIG or language == "English":
            return headline

        try:
            tokenizer, model = load_translator(language)
            if tokenizer is None or model is None:
                return headline

            batch = tokenizer(
                [headline],
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=128,
            )
            generated = model.generate(**batch, max_length=128)
            return tokenizer.batch_decode(generated, skip_special_tokens=True)[0]
        except Exception:
            return headline


    def translate_articles(articles: list[dict], language: str) -> list[dict]:
        translated = []
        for article in articles or []:
            enriched = dict(article)
            enriched["translated_headline"] = translate_headline(
                article.get("headline", ""),
                language,
            )
            translated.append(enriched)
        return translated
    '''
).strip("\n")


VISUALIZATIONS = textwrap.dedent(
    r'''
    from __future__ import annotations

    import base64
    import io
    import json
    import random
    from datetime import datetime, timezone

    import matplotlib.pyplot as plt
    import numpy as np
    import plotly.graph_objects as go
    from wordcloud import WordCloud

    from nlp_pipeline import extract_keywords
    from sentiment import sentiment_breakdown


    WORDCLOUD_COLORS = ["#2D8A70", "#1A1A1A", "#708090"]


    def _wordcloud_color_func(*_args, **_kwargs):
        return random.choice(WORDCLOUD_COLORS)


    def _build_circle_mask(size: int = 700) -> np.ndarray:
        y, x = np.ogrid[:size, :size]
        center = (size - 1) / 2
        radius = size / 2.25
        mask = np.where((x - center) ** 2 + (y - center) ** 2 > radius ** 2, 255, 0)
        return mask.astype(np.uint8)


    def generate_wordcloud(articles: list[dict]) -> str | None:
        text = " ".join(article.get("headline", "") for article in articles or [])
        if not text.strip():
            return None

        mask = _build_circle_mask()
        cloud = WordCloud(
            width=900,
            height=900,
            background_color=None,
            mode="RGBA",
            mask=mask,
            contour_width=0,
            max_words=180,
            collocations=False,
        ).generate(text)
        cloud.recolor(color_func=_wordcloud_color_func)

        fig, ax = plt.subplots(figsize=(7, 7), facecolor="none")
        fig.patch.set_alpha(0)
        ax.set_facecolor("none")
        ax.imshow(cloud, interpolation="bilinear")
        ax.axis("off")

        buffer = io.BytesIO()
        plt.tight_layout(pad=0)
        plt.savefig(buffer, format="png", bbox_inches="tight", transparent=True)
        plt.close(fig)
        encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return f"data:image/png;base64,{encoded}"


    def generate_sentiment_pie(articles: list[dict]) -> dict:
        breakdown = sentiment_breakdown(articles)
        counts = breakdown["counts"]

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=list(counts.keys()),
                    values=list(counts.values()),
                    hole=0.62,
                    marker=dict(colors=["#5aa469", "#d65d5d", "#b0a99f"]),
                    textinfo="label+percent",
                )
            ]
        )
        fig.update_layout(
            title="Sentiment Distribution",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=0, b=0),
            font=dict(family="Inter, sans-serif"),
        )
        return json.loads(fig.to_json())


    def generate_keyword_bar(articles: list[dict]) -> dict:
        keywords = extract_keywords(articles, top_n=15)
        terms = [item["term"].title() for item in keywords]
        counts = [item["count"] for item in keywords]

        fig = go.Figure(
            data=[
                go.Bar(
                    x=counts,
                    y=terms,
                    orientation="h",
                    marker=dict(
                        color=counts,
                        colorscale=[
                            [0.0, "#7b5b20"],
                            [0.5, "#b8892d"],
                            [1.0, "#e1bc5c"],
                        ],
                    ),
                )
            ]
        )
        fig.update_layout(
            title="Top Keywords",
            yaxis=dict(autorange="reversed"),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=0, b=0),
            font=dict(family="Inter, sans-serif"),
        )
        return json.loads(fig.to_json())


    def generate_sentiment_scatter(articles: list[dict]) -> dict:
        ordered = sorted(articles or [], key=lambda item: item.get("timestamp", 0))
        x_values = []
        y_values = []
        colors = []
        labels = []

        for article in ordered:
            timestamp = article.get("timestamp")
            if timestamp:
                dt = datetime.fromtimestamp(timestamp, tz=timezone.utc)
                x_values.append(dt.isoformat())
            else:
                x_values.append(article.get("published_iso", ""))

            score = article.get("sentiment_score", 0.0)
            y_values.append(score)
            labels.append(article.get("headline", ""))

            sentiment = article.get("sentiment", "Neutral")
            if sentiment == "Positive":
                colors.append("#4f9d69")
            elif sentiment == "Negative":
                colors.append("#d4685d")
            else:
                colors.append("#8b847e")

        fig = go.Figure(
            data=[
                go.Scatter(
                    x=x_values,
                    y=y_values,
                    mode="markers",
                    marker=dict(size=11, color=colors, line=dict(width=1, color="#ffffff")),
                    text=labels,
                    hovertemplate="%{text}<br>Score: %{y}<extra></extra>",
                )
            ]
        )
        fig.add_hline(y=0.05, line_dash="dash", line_color="#5aa469")
        fig.add_hline(y=-0.05, line_dash="dash", line_color="#d65d5d")
        fig.update_layout(
            title="Sentiment Score Over Time",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis_title="Publication Time",
            yaxis_title="VADER Compound Score",
            font=dict(family="Inter, sans-serif"),
        )
        return json.loads(fig.to_json())


    def build_visual_payload(articles: list[dict]) -> dict:
        return {
            "wordcloud": generate_wordcloud(articles),
            "pie": generate_sentiment_pie(articles),
            "bar": generate_keyword_bar(articles),
            "scatter": generate_sentiment_scatter(articles),
        }
    '''
).strip("\n")


AGENT = textwrap.dedent(
    r'''
    from __future__ import annotations

    import re
    from collections import Counter
    from dataclasses import dataclass, field
    from statistics import mean
    from threading import Lock

    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

    from fetch_news import fetch_news
    from nlp_pipeline import assess_topic_specificity, generate_briefing
    from sentiment import process_articles


    FLAN_MODEL_NAME = "google/flan-t5-base"
    TOOL_REGISTRY = {
        "search_news": "Fetches the latest Google News RSS results for a query.",
        "assess_quality": "Evaluates whether fetched headlines are numerous and relevant enough.",
        "refine_query": "Narrows the query when the fetched headlines drift away from the topic.",
        "broaden_query": "Broadens the query when too few articles are returned.",
        "analyze_sentiment": "Runs VADER sentiment classification on every headline.",
        "summarize": "Builds a short TextRank-style briefing for the accepted articles.",
    }

    STOPWORDS = {
        "the",
        "a",
        "an",
        "and",
        "or",
        "of",
        "for",
        "to",
        "in",
        "on",
        "at",
        "by",
        "from",
        "with",
        "latest",
        "news",
        "update",
        "updates",
        "today",
        "breaking",
    }

    VAGUE_EXPANSIONS = {
        "ai": "artificial intelligence latest news",
        "technology": "technology industry latest news",
        "economy": "global economy latest news",
        "markets": "stock market latest news",
        "sports": "sports latest news",
        "weather": "extreme weather latest news",
        "politics": "politics latest news",
        "business": "business latest news",
    }

    _flan_tokenizer = None
    _flan_model = None
    _flan_failed = False
    _flan_lock = Lock()


    def load_flan():
        global _flan_tokenizer, _flan_model, _flan_failed
        if _flan_failed:
            return None, None
        if _flan_tokenizer is not None and _flan_model is not None:
            return _flan_tokenizer, _flan_model
        with _flan_lock:
            if _flan_failed:
                return None, None
            if _flan_tokenizer is not None and _flan_model is not None:
                return _flan_tokenizer, _flan_model
            try:
                _flan_tokenizer = AutoTokenizer.from_pretrained(FLAN_MODEL_NAME)
                _flan_model = AutoModelForSeq2SeqLM.from_pretrained(FLAN_MODEL_NAME)
                return _flan_tokenizer, _flan_model
            except Exception:
                _flan_failed = True
                return None, None


    def flan_reason(prompt: str, max_new_tokens: int = 32) -> str:
        tokenizer, model = load_flan()
        if tokenizer is None or model is None:
            return ""
        try:
            encoded = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
            generated = model.generate(**encoded, max_new_tokens=max_new_tokens)
            return tokenizer.decode(generated[0], skip_special_tokens=True).strip()
        except Exception:
            return ""


    def _tokenize(value: str) -> list[str]:
        return [
            token.lower()
            for token in re.findall(r"[A-Za-z0-9]+", value or "")
            if token.lower() not in STOPWORDS
        ]


    def headline_relevance(headline: str, topic: str) -> float:
        topic_tokens = set(_tokenize(topic))
        headline_tokens = set(_tokenize(headline))
        if not topic_tokens:
            return 0.0
        overlap = len(topic_tokens & headline_tokens) / len(topic_tokens)
        if (topic or "").strip().lower() in (headline or "").strip().lower():
            overlap = max(overlap, 0.75)
        return round(overlap, 3)


    def _extract_candidate_terms(articles: list[dict], topic: str) -> list[str]:
        topic_tokens = set(_tokenize(topic))
        counter = Counter()
        for article in articles or []:
            for token in _tokenize(article.get("headline", "")):
                if token not in topic_tokens and len(token) > 2:
                    counter[token] += 1
        return [term for term, _count in counter.most_common(5)]


    def _heuristic_expand_query(topic: str, specificity: str) -> str:
        lowered = (topic or "").strip().lower()
        if specificity in {"specific", "person"}:
            return topic
        return VAGUE_EXPANSIONS.get(lowered, f"{topic} latest news")


    def agent_expand_query(topic: str, specificity: str) -> str:
        baseline = _heuristic_expand_query(topic, specificity)
        if specificity in {"specific", "person"}:
            return baseline

        prompt = f"""
        Rewrite this vague news topic into one concise search query for Google News.
        Topic: {topic}
        Keep it under 8 words and preserve the user's meaning.
        """
        candidate = flan_reason(prompt, max_new_tokens=20)
        if candidate:
            candidate = candidate.splitlines()[0].strip(" -:;")
        return candidate or baseline


    def _heuristic_quality_decision(articles: list[dict], topic: str) -> dict:
        count = len(articles or [])
        relevance_scores = [headline_relevance(item.get("headline", ""), topic) for item in articles or []]
        avg_relevance = round(mean(relevance_scores), 3) if relevance_scores else 0.0

        if count == 0:
            decision = "broaden"
            reason = "No articles came back, so the agent needs a broader query."
        elif count < 3:
            decision = "broaden"
            reason = "Too few articles were returned, so the query should be broadened."
        elif avg_relevance < 0.16:
            decision = "refine"
            reason = "The headlines drift away from the topic, so the query should be refined."
        else:
            decision = "accept"
            reason = "The article count and relevance are strong enough to continue."

        return {
            "decision": decision,
            "reason": reason,
            "count": count,
            "avg_relevance": avg_relevance,
        }


    def agent_assess_quality(articles: list[dict], topic: str) -> dict:
        heuristic = _heuristic_quality_decision(articles, topic)
        prompt = f"""
        You are assessing the quality of a news search.
        Topic: {topic}
        Articles found: {heuristic['count']}
        Average headline relevance: {heuristic['avg_relevance']}
        Choose one action: ACCEPT, BROADEN, or REFINE.
        Then give a short reason.
        """
        candidate = flan_reason(prompt, max_new_tokens=24).upper()
        if "ACCEPT" in candidate:
            heuristic["decision"] = "accept"
        elif "BROADEN" in candidate:
            heuristic["decision"] = "broaden"
        elif "REFINE" in candidate:
            heuristic["decision"] = "refine"

        if candidate:
            heuristic["reason"] = candidate.title()
        return heuristic


    def _heuristic_refined_query(current_query: str, articles: list[dict], mode: str, original_topic: str) -> str:
        if mode == "broaden":
            if "latest news" not in current_query.lower():
                return f"{original_topic} latest news"
            parts = current_query.split()
            if len(parts) > 2:
                return " ".join(parts[:2] + ["news"])
            return current_query

        candidate_terms = _extract_candidate_terms(articles, original_topic)
        if candidate_terms:
            return f"{original_topic} {candidate_terms[0]} news"
        return f"{original_topic} latest updates"


    def agent_refine_query(current_query: str, articles: list[dict], mode: str, original_topic: str) -> str:
        baseline = _heuristic_refined_query(current_query, articles, mode, original_topic)
        prompt = f"""
        Improve this Google News query.
        Original topic: {original_topic}
        Current query: {current_query}
        Mode: {mode}
        Sample headlines: {[item.get('headline', '') for item in articles[:5]]}
        Return only one short query under 10 words.
        """
        candidate = flan_reason(prompt, max_new_tokens=20)
        if candidate:
            candidate = candidate.splitlines()[0].strip(" -:;")
        return candidate or baseline


    @dataclass
    class VeritasAgent:
        max_attempts: int = 3
        reasoning_log: list[dict] = field(default_factory=list)

        def _log(self, stage: str, message: str, tool: str | None = None) -> None:
            entry = {"stage": stage, "message": message}
            if tool:
                entry["tool"] = tool
            self.reasoning_log.append(entry)

        def run(self, topic: str) -> dict:
            self.reasoning_log = []
            topic = (topic or "").strip()
            specificity = assess_topic_specificity(topic)
            self._log("observe", f"Classified topic specificity as {specificity}.")

            query = agent_expand_query(topic, specificity)
            if query == topic:
                self._log("reason", "Topic is already specific enough, so the first search uses it directly.")
            else:
                self._log(
                    "reason",
                    f"Topic is broad, so the agent expanded it to '{query}'.",
                    tool="refine_query",
                )

            best_articles: list[dict] = []

            for attempt in range(1, self.max_attempts + 1):
                self._log(
                    "act",
                    f"Attempt {attempt}: searching Google News for '{query}'.",
                    tool="search_news",
                )
                raw_articles = fetch_news(query, max_articles=15, display_topic=topic)
                self._log("observe", f"Retrieved {len(raw_articles)} candidate articles.")

                assessment = agent_assess_quality(raw_articles, topic)
                self._log(
                    "reason",
                    (
                        f"Quality decision: {assessment['decision']} "
                        f"(count={assessment['count']}, relevance={assessment['avg_relevance']}). "
                        f"{assessment['reason']}"
                    ),
                    tool="assess_quality",
                )

                best_articles = raw_articles
                if assessment["decision"] == "accept":
                    break

                if attempt < self.max_attempts:
                    next_query = agent_refine_query(
                        current_query=query,
                        articles=raw_articles,
                        mode=assessment["decision"],
                        original_topic=topic,
                    )
                    tool_name = "broaden_query" if assessment["decision"] == "broaden" else "refine_query"
                    self._log(
                        "act",
                        f"Adjusting the query to '{next_query}' before the next retry.",
                        tool=tool_name,
                    )
                    query = next_query
                else:
                    self._log(
                        "reason",
                        "Maximum retries reached, so the agent will continue with the best available set.",
                    )

            processed = process_articles(best_articles, limit_per_topic=10)
            self._log(
                "act",
                f"Computed VADER sentiment for {len(processed)} accepted articles.",
                tool="analyze_sentiment",
            )
            self._log(
                "act",
                "Prepared the final briefing summary for this topic.",
                tool="summarize",
            )

            return {
                "topic": topic,
                "query": query,
                "articles": processed,
                "briefing": generate_briefing(processed),
                "reasoning": list(self.reasoning_log),
            }


    def run_agent_for_topics(topics: list[str]) -> dict:
        clean_topics = [(topic or "").strip() for topic in topics or [] if (topic or "").strip()][:3]
        all_articles: list[dict] = []
        reasoning_log: dict[str, list[dict]] = {}
        topic_briefings: dict[str, str] = {}

        for topic in clean_topics:
            agent = VeritasAgent(max_attempts=3)
            result = agent.run(topic)
            all_articles.extend(result["articles"])
            reasoning_log[topic] = result["reasoning"]
            topic_briefings[topic] = result["briefing"]

        all_articles.sort(key=lambda item: item.get("timestamp", 0), reverse=True)
        return {
            "articles": all_articles,
            "briefing": generate_briefing(all_articles),
            "topics": clean_topics,
            "reasoning_log": reasoning_log,
            "topic_briefings": topic_briefings,
            "tool_registry": TOOL_REGISTRY,
        }
    '''
).strip("\n")


CHATBOT = textwrap.dedent(
    r'''
    from __future__ import annotations

    import re

    from fetch_news import fetch_news
    from nlp_pipeline import (
        extract_entities_from_query,
        extract_followup_suggestions,
        generate_briefing,
    )
    from sentiment import process_articles, sentiment_breakdown


    FOLLOWUP_PHRASES = {
        "stock": "stock price",
        "price": "stock price",
        "shares": "stock price",
        "earnings": "earnings",
        "guidance": "guidance",
        "lawsuit": "lawsuit",
        "acquisition": "acquisition",
        "flood": "flood updates",
        "weather": "weather impact",
    }


    def get_sentiment_tone(articles: list[dict]) -> str:
        breakdown = sentiment_breakdown(articles)
        positives = breakdown["percentages"].get("Positive", 0.0)
        negatives = breakdown["percentages"].get("Negative", 0.0)
        if negatives > positives + 15:
            return "The overall tone in the latest coverage is leaning negative right now."
        if positives > negatives + 15:
            return "The overall tone in the latest coverage is leaning positive right now."
        return "The latest coverage is fairly mixed right now."


    def is_briefing_request(message: str) -> bool:
        lowered = (message or "").lower()
        triggers = {"brief", "briefing", "summary", "summarize", "recap", "what is happening"}
        return any(trigger in lowered for trigger in triggers)


    def _format_breakdown_line(articles: list[dict]) -> str:
        breakdown = sentiment_breakdown(articles)
        percentages = breakdown["percentages"]
        return (
            f"{percentages.get('Positive', 0.0)}% Positive, "
            f"{percentages.get('Negative', 0.0)}% Negative, "
            f"{percentages.get('Neutral', 0.0)}% Neutral."
        )


    def format_article_list(articles: list[dict], limit: int = 3) -> list[dict]:
        rendered = []
        for article in articles[:limit]:
            rendered.append(
                {
                    "headline": article.get("headline", ""),
                    "translated_headline": article.get("translated_headline", article.get("headline", "")),
                    "link": article.get("link", ""),
                    "source": article.get("source", ""),
                    "published_display": article.get("published_display", ""),
                    "sentiment": article.get("sentiment", "Neutral"),
                    "topic": article.get("topic", ""),
                }
            )
        return rendered


    def _clean_query_text(message: str) -> str:
        cleaned = re.sub(
            r"(?i)\b(find|show|give|tell|latest|news|on|about|what|is|going|with|please|me|the)\b",
            " ",
            message or "",
        )
        cleaned = re.sub(r"\s+", " ", cleaned).strip(" ?.!,:;")
        return cleaned


    def _resolve_from_history(history: list[dict]) -> str:
        for item in reversed(history or []):
            content = item.get("content", "")
            entities = extract_entities_from_query(content)
            if entities:
                return entities[0]
        return ""


    def resolve_topic(message: str, history: list[dict] | None = None, last_topic: str | None = None) -> str:
        entities = extract_entities_from_query(message)
        if entities:
            return entities[0]

        lowered = (message or "").lower()
        suffixes = [value for key, value in FOLLOWUP_PHRASES.items() if key in lowered]
        if last_topic and (suffixes or re.search(r"\b(it|their|them|that|those|he|she|its)\b", lowered)):
            suffix = suffixes[0] if suffixes else ""
            return f"{last_topic} {suffix}".strip()

        cleaned = _clean_query_text(message)
        if cleaned:
            return cleaned

        if last_topic:
            return last_topic

        return _resolve_from_history(history or [])


    def generate_chatbot_response(
        message: str,
        history: list[dict] | None = None,
        last_topic: str | None = None,
        articles: list[dict] | None = None,
    ) -> dict:
        history = history or []
        current_articles = articles or []
        active_topic = resolve_topic(message, history=history, last_topic=last_topic)

        if is_briefing_request(message) and current_articles:
            tone = get_sentiment_tone(current_articles)
            briefing = generate_briefing(current_articles, sentence_count=3)
            suggestions = extract_followup_suggestions(current_articles, active_topic or last_topic or "")
            return {
                "response": f"{tone} {briefing} {_format_breakdown_line(current_articles)}",
                "last_topic": active_topic or last_topic,
                "suggestions": suggestions,
                "articles": format_article_list(current_articles, limit=3),
                "mode": "briefing",
                "sentiment_commentary": _format_breakdown_line(current_articles),
            }

        if active_topic:
            fresh_articles = process_articles(fetch_news(active_topic, max_articles=10), limit_per_topic=10)
        else:
            fresh_articles = process_articles(current_articles, limit_per_topic=10) if current_articles else []

        if not fresh_articles and current_articles:
            fresh_articles = process_articles(current_articles, limit_per_topic=10)

        if not fresh_articles:
            return {
                "response": "I could not find fresh articles for that topic yet, but you can try a more specific news query next.",
                "last_topic": active_topic or last_topic,
                "suggestions": [],
                "articles": [],
                "mode": "fallback",
                "sentiment_commentary": "0.0% Positive, 0.0% Negative, 0.0% Neutral.",
            }

        tone = get_sentiment_tone(fresh_articles)
        article_cards = format_article_list(fresh_articles, limit=3)
        suggestions = extract_followup_suggestions(fresh_articles, active_topic or last_topic or "")
        sentiment_line = _format_breakdown_line(fresh_articles)
        response = (
            f"{tone} I found recent coverage for {active_topic or last_topic or 'this topic'}. "
            f"Here are a few links to open next. {sentiment_line}"
        )

        return {
            "response": response,
            "last_topic": active_topic or last_topic,
            "suggestions": suggestions,
            "articles": article_cards,
            "mode": "articles",
            "sentiment_commentary": sentiment_line,
        }
    '''
).strip("\n")


TEMPLATES = textwrap.dedent(
    r'''
    HTML_PAGE = r"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>VeritasAI</title>
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
      <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
      <style>
        :root {
          --bg: #f5efe4;
          --bg-deep: #efe2c4;
          --panel: rgba(255, 250, 241, 0.78);
          --panel-strong: rgba(255, 250, 241, 0.94);
          --ink: #171512;
          --muted: #6f675f;
          --gold: #c89f47;
          --gold-deep: #a47d28;
          --positive: #3f8b59;
          --negative: #c85a52;
          --neutral: #8e847b;
          --border: rgba(23, 21, 18, 0.08);
          --shadow: 0 30px 60px rgba(64, 44, 11, 0.12);
        }

        * {
          box-sizing: border-box;
        }

        body {
          margin: 0;
          min-height: 100vh;
          font-family: "Sora", sans-serif;
          color: var(--ink);
          background:
            radial-gradient(circle at top left, rgba(240, 208, 132, 0.5), transparent 30%),
            radial-gradient(circle at bottom right, rgba(90, 71, 33, 0.10), transparent 25%),
            linear-gradient(135deg, #f8f4ec 0%, #f0e1c1 100%);
        }

        .app-shell {
          max-width: 1500px;
          margin: 0 auto;
          padding: 28px 20px 40px;
        }

        .masthead {
          display: grid;
          grid-template-columns: 1.4fr 0.8fr;
          gap: 24px;
          margin-bottom: 24px;
          animation: riseIn 0.6s ease;
        }

        .hero-panel,
        .side-stat {
          border: 1px solid var(--border);
          background: var(--panel);
          backdrop-filter: blur(18px);
          border-radius: 28px;
          box-shadow: var(--shadow);
          overflow: hidden;
          position: relative;
        }

        .hero-panel {
          padding: 28px;
          background:
            linear-gradient(135deg, rgba(14, 14, 14, 0.92), rgba(48, 36, 22, 0.84)),
            linear-gradient(120deg, rgba(200, 159, 71, 0.35), transparent 55%);
          color: #f7f1e3;
        }

        .hero-panel::after {
          content: "";
          position: absolute;
          inset: auto -80px -80px auto;
          width: 240px;
          height: 240px;
          border-radius: 50%;
          background: radial-gradient(circle, rgba(200, 159, 71, 0.35), transparent 68%);
        }

        .eyebrow {
          text-transform: uppercase;
          letter-spacing: 0.18em;
          font-size: 0.78rem;
          opacity: 0.8;
          margin-bottom: 14px;
        }

        .hero-title {
          font-size: clamp(2rem, 4vw, 3.6rem);
          line-height: 1.05;
          margin: 0 0 14px;
          max-width: 12ch;
        }

        .hero-subtitle {
          max-width: 62ch;
          color: rgba(247, 241, 227, 0.86);
          line-height: 1.7;
          margin: 0 0 24px;
        }

        .hero-tags {
          display: flex;
          flex-wrap: wrap;
          gap: 10px;
        }

        .hero-tag,
        .pill {
          display: inline-flex;
          align-items: center;
          gap: 8px;
          border-radius: 999px;
          padding: 10px 14px;
          font-size: 0.86rem;
          border: 1px solid rgba(255, 255, 255, 0.14);
          background: rgba(255, 255, 255, 0.07);
        }

        .side-stat {
          padding: 24px;
          display: grid;
          gap: 18px;
          background:
            linear-gradient(180deg, rgba(255, 248, 235, 0.95), rgba(248, 236, 210, 0.88));
        }

        .stat-card {
          padding: 18px;
          border-radius: 20px;
          background: rgba(255, 255, 255, 0.56);
          border: 1px solid rgba(23, 21, 18, 0.06);
        }

        .stat-label {
          font-size: 0.85rem;
          color: var(--muted);
          margin-bottom: 6px;
        }

        .stat-value {
          font-size: 1.7rem;
          font-weight: 700;
        }

        .layout {
          display: grid;
          grid-template-columns: minmax(0, 1.55fr) minmax(320px, 0.78fr);
          gap: 24px;
          align-items: start;
        }

        .stack {
          display: grid;
          gap: 24px;
        }

        .panel {
          border-radius: 26px;
          border: 1px solid var(--border);
          background: var(--panel-strong);
          box-shadow: var(--shadow);
          overflow: hidden;
        }

        .panel-body {
          padding: 22px;
        }

        .section-title {
          margin: 0 0 6px;
          font-size: 1.1rem;
        }

        .section-copy {
          margin: 0;
          color: var(--muted);
          line-height: 1.7;
          font-size: 0.94rem;
        }

        .input-grid {
          display: grid;
          grid-template-columns: repeat(3, minmax(0, 1fr));
          gap: 14px;
          margin: 18px 0 14px;
        }

        .field {
          display: grid;
          gap: 7px;
        }

        .field label {
          font-size: 0.86rem;
          color: var(--muted);
        }

        .field input,
        .field select,
        .chat-input {
          width: 100%;
          border: 1px solid rgba(23, 21, 18, 0.1);
          border-radius: 16px;
          padding: 14px 15px;
          font: inherit;
          background: rgba(255, 255, 255, 0.9);
          color: var(--ink);
          outline: none;
          transition: border-color 0.2s ease, transform 0.2s ease;
        }

        .field input:focus,
        .field select:focus,
        .chat-input:focus {
          border-color: var(--gold);
          transform: translateY(-1px);
        }

        .controls {
          display: flex;
          flex-wrap: wrap;
          gap: 12px;
          align-items: center;
          justify-content: space-between;
        }

        .button-row {
          display: flex;
          gap: 10px;
          flex-wrap: wrap;
        }

        button {
          cursor: pointer;
          border: none;
          border-radius: 999px;
          font: inherit;
          transition: transform 0.2s ease, opacity 0.2s ease, box-shadow 0.2s ease;
        }

        button:hover {
          transform: translateY(-1px);
        }

        .primary-btn {
          padding: 13px 18px;
          background: linear-gradient(135deg, #151515, #433118);
          color: #fffaf0;
          box-shadow: 0 15px 30px rgba(58, 38, 10, 0.18);
        }

        .ghost-btn {
          padding: 12px 16px;
          background: rgba(200, 159, 71, 0.12);
          color: var(--ink);
        }

        .status-pill {
          padding: 10px 14px;
          border-radius: 999px;
          background: rgba(200, 159, 71, 0.14);
          color: #5d471e;
          font-size: 0.9rem;
        }

        .ticker-wrap {
          overflow: hidden;
          border-top: 1px solid rgba(23, 21, 18, 0.06);
          border-bottom: 1px solid rgba(23, 21, 18, 0.06);
          background: rgba(23, 21, 18, 0.03);
          height: 52px;
          display: flex;
          align-items: center;
        }

        .ticker-track {
          white-space: nowrap;
          display: inline-flex;
          gap: 28px;
          padding-left: 18px;
          animation: tickerMove 28s linear infinite;
          font-size: 0.92rem;
          color: #4b4239;
        }

        .ticker-item strong {
          color: var(--gold-deep);
          margin-right: 8px;
        }

        .brief-card {
          display: none;
          padding: 24px;
          background:
            linear-gradient(145deg, #151515, #2a231b),
            radial-gradient(circle at top left, rgba(200, 159, 71, 0.24), transparent 35%);
          color: #f7f1e3;
        }

        .brief-card.visible {
          display: block;
        }

        .brief-card p {
          margin: 10px 0 0;
          line-height: 1.8;
          color: rgba(247, 241, 227, 0.92);
        }

        .chip-row {
          display: flex;
          flex-wrap: wrap;
          gap: 10px;
          margin-top: 18px;
        }

        .topic-chip,
        .suggestion-chip {
          padding: 10px 14px;
          border-radius: 999px;
          background: rgba(200, 159, 71, 0.12);
          color: #60491d;
          font-size: 0.85rem;
          border: 1px solid rgba(200, 159, 71, 0.16);
        }

        .results-grid {
          display: grid;
          gap: 18px;
        }

        .hero-article {
          display: none;
          min-height: 280px;
          position: relative;
          padding: 24px;
          border-radius: 24px;
          overflow: hidden;
          color: #f8f4ea;
          background:
            linear-gradient(135deg, rgba(17, 17, 17, 0.96), rgba(58, 40, 16, 0.88)),
            linear-gradient(120deg, rgba(200, 159, 71, 0.28), transparent 45%);
        }

        .hero-article.visible {
          display: block;
        }

        .hero-article h3 {
          margin: 10px 0 12px;
          font-size: clamp(1.5rem, 3vw, 2.4rem);
          max-width: 16ch;
          line-height: 1.15;
        }

        .hero-article a {
          color: inherit;
          text-decoration: none;
        }

        .meta-row {
          display: flex;
          flex-wrap: wrap;
          gap: 10px;
          font-size: 0.86rem;
          color: rgba(248, 244, 234, 0.76);
        }

        .article-grid {
          display: grid;
          grid-template-columns: repeat(3, minmax(0, 1fr));
          gap: 16px;
        }

        .article-card,
        .chat-card {
          position: relative;
          padding: 18px 18px 18px 22px;
          border-radius: 22px;
          background: rgba(255, 255, 255, 0.92);
          border: 1px solid rgba(23, 21, 18, 0.06);
          min-height: 190px;
          box-shadow: 0 18px 32px rgba(69, 49, 17, 0.08);
          overflow: hidden;
        }

        .article-card::before,
        .chat-card::before {
          content: "";
          position: absolute;
          left: 0;
          top: 0;
          bottom: 0;
          width: 6px;
          background: var(--neutral);
        }

        .article-card.positive::before,
        .chat-card.positive::before {
          background: var(--positive);
        }

        .article-card.negative::before,
        .chat-card.negative::before {
          background: var(--negative);
        }

        .article-card.neutral::before,
        .chat-card.neutral::before {
          background: var(--neutral);
        }

        .article-card h4,
        .chat-card h4 {
          margin: 10px 0 12px;
          line-height: 1.5;
          font-size: 1rem;
        }

        .article-card a,
        .chat-card a {
          color: var(--ink);
          text-decoration: none;
        }

        .article-card a:hover,
        .chat-card a:hover {
          color: var(--gold-deep);
        }

        .badge {
          display: inline-flex;
          align-items: center;
          padding: 7px 10px;
          border-radius: 999px;
          font-size: 0.76rem;
          font-weight: 600;
          letter-spacing: 0.02em;
        }

        .badge.positive {
          background: rgba(63, 139, 89, 0.14);
          color: #2f6f45;
        }

        .badge.negative {
          background: rgba(200, 90, 82, 0.14);
          color: #9f433c;
        }

        .badge.neutral {
          background: rgba(142, 132, 123, 0.14);
          color: #756a61;
        }

        .card-meta {
          display: flex;
          flex-wrap: wrap;
          gap: 8px 14px;
          color: var(--muted);
          font-size: 0.82rem;
        }

        .visual-grid {
          display: grid;
          grid-template-columns: repeat(2, minmax(0, 1fr));
          gap: 16px;
          margin-top: 18px;
        }

        .visual-card {
          min-height: 360px;
          padding: 12px;
          border-radius: 22px;
          border: 1px solid rgba(23, 21, 18, 0.06);
          background: rgba(255, 255, 255, 0.72);
        }

        .wordcloud-frame {
          width: 100%;
          height: 100%;
          min-height: 360px;
          display: grid;
          place-items: center;
        }

        .wordcloud-frame img {
          max-width: 100%;
          border-radius: 18px;
        }

        .side-rail {
          display: grid;
          gap: 24px;
        }

        .log-list {
          display: grid;
          gap: 16px;
        }

        .log-topic {
          padding: 16px;
          border-radius: 20px;
          background: rgba(255, 255, 255, 0.65);
          border: 1px solid rgba(23, 21, 18, 0.05);
        }

        .log-topic h4 {
          margin: 0 0 10px;
          font-size: 1rem;
        }

        .log-item {
          display: grid;
          gap: 5px;
          padding: 10px 0;
          border-top: 1px dashed rgba(23, 21, 18, 0.07);
        }

        .log-item:first-child {
          border-top: none;
          padding-top: 0;
        }

        .log-stage {
          text-transform: uppercase;
          letter-spacing: 0.12em;
          font-size: 0.72rem;
          color: var(--gold-deep);
        }

        .log-message {
          font-size: 0.89rem;
          line-height: 1.65;
          color: #403830;
        }

        .chat-shell {
          display: grid;
          gap: 14px;
        }

        .chat-messages {
          min-height: 280px;
          max-height: 560px;
          overflow-y: auto;
          display: grid;
          gap: 12px;
          padding-right: 6px;
        }

        .bubble {
          padding: 14px 16px;
          border-radius: 18px;
          font-size: 0.92rem;
          line-height: 1.7;
        }

        .bubble.user {
          background: #171512;
          color: #f7f1e3;
          justify-self: end;
          max-width: 90%;
        }

        .bubble.assistant {
          background: rgba(200, 159, 71, 0.12);
          color: var(--ink);
          max-width: 100%;
        }

        .chat-cards {
          display: grid;
          gap: 10px;
          margin-top: 12px;
        }

        .chat-form {
          display: grid;
          gap: 10px;
        }

        .chat-row {
          display: flex;
          gap: 10px;
        }

        .empty-state {
          color: var(--muted);
          font-size: 0.92rem;
          line-height: 1.7;
        }

        .hidden {
          display: none !important;
        }

        @keyframes tickerMove {
          0% { transform: translateX(0); }
          100% { transform: translateX(-50%); }
        }

        @keyframes riseIn {
          from {
            opacity: 0;
            transform: translateY(12px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        @media (max-width: 1180px) {
          .layout,
          .masthead,
          .visual-grid {
            grid-template-columns: 1fr;
          }

          .article-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
          }
        }

        @media (max-width: 720px) {
          .app-shell {
            padding: 16px 14px 30px;
          }

          .input-grid,
          .article-grid,
          .visual-grid {
            grid-template-columns: 1fr;
          }

          .controls,
          .button-row,
          .chat-row {
            flex-direction: column;
            align-items: stretch;
          }

          .hero-title {
            max-width: none;
          }
        }
      </style>
    </head>
    <body>
      <div class="app-shell">
        <section class="masthead">
          <div class="hero-panel">
            <div class="eyebrow">VeritasAI News Agent</div>
            <h1 class="hero-title">Adaptive news search, not a fixed pipeline.</h1>
            <p class="hero-subtitle">
              Enter up to three topics and the agent will observe, reason, adjust its search strategy,
              score the sentiment of every headline, build a short briefing, and render interactive visuals.
            </p>
            <div class="hero-tags">
              <span class="hero-tag">Open-source LLM loop</span>
              <span class="hero-tag">Multilingual translation</span>
              <span class="hero-tag">Voyant-inspired visuals</span>
              <span class="hero-tag">Conversational news bot</span>
            </div>
          </div>
          <div class="side-stat">
            <div class="stat-card">
              <div class="stat-label">Runtime stack</div>
              <div class="stat-value">FastAPI + Colab</div>
            </div>
            <div class="stat-card">
              <div class="stat-label">Reasoning engine</div>
              <div class="stat-value">FLAN-T5 Base</div>
            </div>
            <div class="stat-card">
              <div class="stat-label">Current session</div>
              <div class="stat-value" id="sessionSummary">Awaiting topics</div>
            </div>
          </div>
        </section>

        <section class="layout">
          <main class="stack">
            <section class="panel">
              <div class="panel-body">
                <h2 class="section-title">Fetch Live Coverage</h2>
                <p class="section-copy">
                  Add up to three preferences. Specific topics like companies and people are searched directly,
                  while broader topics can be expanded by the agent before retrieval.
                </p>
                <div class="input-grid">
                  <div class="field">
                    <label for="topic1">Topic 1</label>
                    <input id="topic1" placeholder="Nvidia" />
                  </div>
                  <div class="field">
                    <label for="topic2">Topic 2</label>
                    <input id="topic2" placeholder="Floods in Bangladesh" />
                  </div>
                  <div class="field">
                    <label for="topic3">Topic 3</label>
                    <input id="topic3" placeholder="AI" />
                  </div>
                </div>
                <div class="controls">
                  <div class="button-row">
                    <button class="primary-btn" id="fetchBtn">Fetch News</button>
                    <button class="ghost-btn" id="sampleBtn">Load Sample Topics</button>
                  </div>
                  <div class="button-row">
                    <div class="field" style="min-width: 180px;">
                      <label for="languageSelect">Translate Headlines</label>
                      <select id="languageSelect">
                        <option>English</option>
                        <option>Spanish</option>
                        <option>Hindi</option>
                        <option>French</option>
                        <option>German</option>
                      </select>
                    </div>
                    <div class="status-pill" id="statusPill">Ready for a new search</div>
                  </div>
                </div>
              </div>
              <div class="ticker-wrap">
                <div class="ticker-track" id="tickerTrack">
                  <span class="ticker-item"><strong>Live</strong>Add topics to start the rolling headline feed.</span>
                </div>
              </div>
            </section>

            <section class="panel brief-card" id="briefCard">
              <div class="panel-body">
                <div class="eyebrow">News Brief</div>
                <p id="briefText"></p>
                <div class="chip-row" id="topicChips"></div>
              </div>
            </section>

            <section class="results-grid">
              <article class="hero-article" id="heroArticle"></article>
              <div class="article-grid" id="articleGrid"></div>
            </section>

            <section class="panel">
              <div class="panel-body">
                <h2 class="section-title">Voyant-Inspired Visuals</h2>
                <p class="section-copy">
                  These charts update after each successful fetch to show the shape, sentiment, and keyword profile
                  of the live article set.
                </p>
                <div class="visual-grid">
                  <div class="visual-card">
                    <div class="wordcloud-frame" id="wordcloudFrame">
                      <div class="empty-state">The word cloud will appear after the first fetch.</div>
                    </div>
                  </div>
                  <div class="visual-card" id="pieChart"></div>
                  <div class="visual-card" id="barChart"></div>
                  <div class="visual-card" id="scatterChart"></div>
                </div>
              </div>
            </section>
          </main>

          <aside class="side-rail">
            <section class="panel">
              <div class="panel-body">
                <h2 class="section-title">Agent Reasoning Log</h2>
                <p class="section-copy">
                  Every topic shows the observe, reason, and act trail that led to the final result set.
                </p>
                <div class="log-list" id="reasoningLog">
                  <div class="empty-state">The agent steps will appear here after the first run.</div>
                </div>
              </div>
            </section>

            <section class="panel">
              <div class="panel-body">
                <h2 class="section-title">VeritasBot</h2>
                <p class="section-copy">
                  Ask for a briefing, follow-up links, or another news search. The bot keeps the latest topic in memory.
                </p>
                <div class="chat-shell">
                  <div class="chat-messages" id="chatMessages">
                    <div class="bubble assistant">
                      Ask something like “Find news on Intel stock price” or “Give me a briefing.”
                    </div>
                  </div>
                  <div class="chip-row" id="suggestionChips"></div>
                  <form class="chat-form" id="chatForm">
                    <input class="chat-input" id="chatInput" placeholder="Find news on Apple" />
                    <div class="chat-row">
                      <button class="primary-btn" type="submit">Send</button>
                      <button class="ghost-btn" type="button" id="briefingBtn">Quick Briefing</button>
                    </div>
                  </form>
                </div>
              </div>
            </section>
          </aside>
        </section>
      </div>

      <script>
        const appState = {
          articles: [],
          originalArticles: [],
          history: [],
          lastTopic: null,
          reasoningLog: {},
          briefing: "",
        };

        const statusPill = document.getElementById("statusPill");
        const briefCard = document.getElementById("briefCard");
        const briefText = document.getElementById("briefText");
        const topicChips = document.getElementById("topicChips");
        const heroArticle = document.getElementById("heroArticle");
        const articleGrid = document.getElementById("articleGrid");
        const tickerTrack = document.getElementById("tickerTrack");
        const reasoningLog = document.getElementById("reasoningLog");
        const chatMessages = document.getElementById("chatMessages");
        const suggestionChips = document.getElementById("suggestionChips");
        const sessionSummary = document.getElementById("sessionSummary");

        function escapeHtml(value) {
          return String(value || "")
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
        }

        function sentimentClass(sentiment) {
          const lowered = String(sentiment || "Neutral").toLowerCase();
          if (lowered.includes("positive")) return "positive";
          if (lowered.includes("negative")) return "negative";
          return "neutral";
        }

        async function postJSON(url, payload) {
          const response = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
          });
          if (!response.ok) {
            const text = await response.text();
            throw new Error(text || `Request failed for ${url}`);
          }
          return response.json();
        }

        function setStatus(message) {
          statusPill.textContent = message;
        }

        function renderTicker(articles) {
          if (!articles.length) {
            tickerTrack.innerHTML = '<span class="ticker-item"><strong>Live</strong>Add topics to start the rolling headline feed.</span>';
            return;
          }

          const items = articles.slice(0, 12).map((article) => {
            const headline = article.translated_headline || article.headline;
            return `<span class="ticker-item"><strong>${escapeHtml(article.topic)}</strong>${escapeHtml(headline)}</span>`;
          });
          tickerTrack.innerHTML = [...items, ...items].join("");
        }

        function renderBriefing(briefing, topics) {
          if (!briefing) {
            briefCard.classList.remove("visible");
            return;
          }

          briefCard.classList.add("visible");
          briefText.textContent = briefing;
          topicChips.innerHTML = topics.map((topic) => `<span class="topic-chip">${escapeHtml(topic)}</span>`).join("");
        }

        function articleMarkup(article, featured = false) {
          const cls = sentimentClass(article.sentiment);
          const headline = article.translated_headline || article.headline;
          const wrapperClass = featured ? "hero" : "article-card";
          if (featured) {
            return `
              <div class="eyebrow">${escapeHtml(article.topic || "Top Story")}</div>
              <div class="meta-row">
                <span>${escapeHtml(article.source || "Unknown Source")}</span>
                <span>${escapeHtml(article.published_display || "")}</span>
                <span class="badge ${cls}">${escapeHtml(article.sentiment || "Neutral")}</span>
              </div>
              <h3><a href="${escapeHtml(article.link)}" target="_blank" rel="noopener noreferrer">${escapeHtml(headline)}</a></h3>
              <p style="max-width:58ch; line-height:1.8; color: rgba(248, 244, 234, 0.84);">
                The most recent accepted article across all selected topics appears here as the lead story.
              </p>
            `;
          }

          return `
            <article class="article-card ${cls}">
              <span class="badge ${cls}">${escapeHtml(article.sentiment || "Neutral")}</span>
              <h4><a href="${escapeHtml(article.link)}" target="_blank" rel="noopener noreferrer">${escapeHtml(headline)}</a></h4>
              <div class="card-meta">
                <span>${escapeHtml(article.source || "Unknown Source")}</span>
                <span>${escapeHtml(article.published_display || "")}</span>
                <span>${escapeHtml(article.topic || "")}</span>
              </div>
            </article>
          `;
        }

        function renderArticles(articles) {
          if (!articles.length) {
            heroArticle.classList.remove("visible");
            heroArticle.innerHTML = "";
            articleGrid.innerHTML = '<div class="empty-state">No articles yet. Run the agent to populate the news grid.</div>';
            return;
          }

          const [lead, ...rest] = articles;
          heroArticle.classList.add("visible");
          heroArticle.innerHTML = articleMarkup(lead, true);
          articleGrid.innerHTML = rest.length
            ? rest.map((article) => articleMarkup(article)).join("")
            : '<div class="empty-state">Only one article is available right now, so it is featured above.</div>';
        }

        function renderReasoning(logByTopic) {
          const topics = Object.keys(logByTopic || {});
          if (!topics.length) {
            reasoningLog.innerHTML = '<div class="empty-state">The agent steps will appear here after the first run.</div>';
            return;
          }

          reasoningLog.innerHTML = topics
            .map((topic) => {
              const items = (logByTopic[topic] || []).map((entry) => `
                <div class="log-item">
                  <div class="log-stage">${escapeHtml(entry.stage || "step")}${entry.tool ? ` · ${escapeHtml(entry.tool)}` : ""}</div>
                  <div class="log-message">${escapeHtml(entry.message || "")}</div>
                </div>
              `).join("");
              return `
                <section class="log-topic">
                  <h4>${escapeHtml(topic)}</h4>
                  ${items}
                </section>
              `;
            })
            .join("");
        }

        function renderWordcloud(dataUrl) {
          const frame = document.getElementById("wordcloudFrame");
          if (!dataUrl) {
            frame.innerHTML = '<div class="empty-state">The word cloud will appear after the first fetch.</div>';
            return;
          }
          frame.innerHTML = `<img src="${dataUrl}" alt="Word cloud" />`;
        }

        function renderPlot(targetId, figure) {
          if (!figure) return;
          Plotly.react(targetId, figure.data, figure.layout, {
            displayModeBar: false,
            responsive: true,
          });
        }

        async function fetchVisuals() {
          if (!appState.originalArticles.length) return;
          try {
            const visuals = await postJSON("/visuals", { articles: appState.originalArticles });
            renderWordcloud(visuals.wordcloud);
            renderPlot("pieChart", visuals.pie);
            renderPlot("barChart", visuals.bar);
            renderPlot("scatterChart", visuals.scatter);
          } catch (error) {
            console.error(error);
          }
        }

        function appendBubble(role, html) {
          const bubble = document.createElement("div");
          bubble.className = `bubble ${role}`;
          bubble.innerHTML = html;
          chatMessages.appendChild(bubble);
          chatMessages.scrollTop = chatMessages.scrollHeight;
        }

        function renderSuggestionChips(items) {
          suggestionChips.innerHTML = (items || [])
            .map((item) => `<button class="suggestion-chip" type="button" data-chip="${escapeHtml(item)}">${escapeHtml(item)}</button>`)
            .join("");
        }

        function assistantMarkup(payload) {
          const cards = (payload.articles || []).map((article) => `
            <article class="chat-card ${sentimentClass(article.sentiment)}">
              <span class="badge ${sentimentClass(article.sentiment)}">${escapeHtml(article.sentiment || "Neutral")}</span>
              <h4><a href="${escapeHtml(article.link)}" target="_blank" rel="noopener noreferrer">${escapeHtml(article.translated_headline || article.headline)}</a></h4>
              <div class="card-meta">
                <span>${escapeHtml(article.source || "")}</span>
                <span>${escapeHtml(article.published_display || "")}</span>
              </div>
            </article>
          `).join("");

          return `
            <div>${escapeHtml(payload.response || "")}</div>
            ${cards ? `<div class="chat-cards">${cards}</div>` : ""}
          `;
        }

        async function runFetch() {
          const topics = [1, 2, 3]
            .map((index) => document.getElementById(`topic${index}`).value.trim())
            .filter(Boolean)
            .slice(0, 3);

          if (!topics.length) {
            setStatus("Please enter at least one topic");
            return;
          }

          setStatus("Agent is searching and reasoning...");
          try {
            const payload = await postJSON("/fetch", { topics });
            appState.originalArticles = payload.articles || [];
            appState.articles = payload.articles || [];
            appState.reasoningLog = payload.reasoning_log || {};
            appState.briefing = payload.briefing || "";
            renderBriefing(appState.briefing, payload.topics || topics);
            renderArticles(appState.articles);
            renderReasoning(appState.reasoningLog);
            renderTicker(appState.articles);
            sessionSummary.textContent = `${appState.articles.length} accepted articles`;
            setStatus(`Loaded ${appState.articles.length} articles`);
            await fetchVisuals();
          } catch (error) {
            console.error(error);
            setStatus("Something went wrong while fetching live coverage");
          }
        }

        async function translateArticles(language) {
          if (!appState.originalArticles.length) return;

          if (language === "English") {
            appState.articles = [...appState.originalArticles];
            renderArticles(appState.articles);
            renderTicker(appState.articles);
            setStatus("Showing original English headlines");
            return;
          }

          setStatus(`Translating headlines to ${language}...`);
          try {
            const payload = await postJSON("/translate", {
              articles: appState.originalArticles,
              language,
            });
            appState.articles = payload.articles || [];
            renderArticles(appState.articles);
            renderTicker(appState.articles);
            setStatus(`Translated headlines to ${language}`);
          } catch (error) {
            console.error(error);
            setStatus("Translation failed, so the original headlines are still shown");
          }
        }

        async function sendChat(message) {
          if (!message.trim()) return;
          appendBubble("user", escapeHtml(message));
          appState.history.push({ role: "user", content: message });
          document.getElementById("chatInput").value = "";

          try {
            const payload = await postJSON("/chat", {
              message,
              history: appState.history,
              last_topic: appState.lastTopic,
              articles: appState.originalArticles,
            });
            appState.lastTopic = payload.last_topic || appState.lastTopic;
            appState.history.push({ role: "assistant", content: payload.response || "" });
            appendBubble("assistant", assistantMarkup(payload));
            renderSuggestionChips(payload.suggestions || []);
          } catch (error) {
            console.error(error);
            appendBubble("assistant", "I ran into an issue while generating the chat response.");
          }
        }

        document.getElementById("fetchBtn").addEventListener("click", runFetch);

        document.getElementById("sampleBtn").addEventListener("click", () => {
          document.getElementById("topic1").value = "Nvidia";
          document.getElementById("topic2").value = "Floods in Bangladesh";
          document.getElementById("topic3").value = "AI";
          runFetch();
        });

        document.getElementById("languageSelect").addEventListener("change", (event) => {
          translateArticles(event.target.value);
        });

        document.getElementById("chatForm").addEventListener("submit", (event) => {
          event.preventDefault();
          sendChat(document.getElementById("chatInput").value);
        });

        document.getElementById("briefingBtn").addEventListener("click", () => {
          sendChat("Give me a briefing.");
        });

        suggestionChips.addEventListener("click", (event) => {
          const button = event.target.closest("[data-chip]");
          if (!button) return;
          sendChat(button.getAttribute("data-chip"));
        });
      </script>
    </body>
    </html>
    """
    '''
).strip("\n")

TEMPLATES = Path(__file__).with_name("templates.py").read_text(encoding="utf-8").strip("\n")


MAIN = textwrap.dedent(
    r'''
    from __future__ import annotations

    import threading
    from typing import Any

    from fastapi import FastAPI
    from fastapi.concurrency import run_in_threadpool
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.responses import HTMLResponse
    from pydantic import BaseModel, Field

    from agent import load_flan, run_agent_for_topics
    from chatbot import generate_chatbot_response
    from templates import HTML_PAGE
    from translator import translate_articles
    from visualizations import build_visual_payload


    class FetchRequest(BaseModel):
        topics: list[str] = Field(default_factory=list)


    class TranslateRequest(BaseModel):
        articles: list[dict[str, Any]] = Field(default_factory=list)
        language: str = "English"


    class ChatRequest(BaseModel):
        message: str
        history: list[dict[str, Any]] = Field(default_factory=list)
        last_topic: str | None = None
        articles: list[dict[str, Any]] = Field(default_factory=list)


    class VisualRequest(BaseModel):
        articles: list[dict[str, Any]] = Field(default_factory=list)


    app = FastAPI(title="VeritasAI", version="1.0.0")
    WARMUP_STATE = {
        "in_progress": False,
        "ready": False,
        "error": None,
    }
    _warmup_lock = threading.Lock()


    def _warm_agent_models() -> None:
        ready = False
        error_message = None
        try:
            tokenizer, model = load_flan()
            ready = tokenizer is not None and model is not None
            if not ready:
                error_message = "Warm-up could not load the FLAN model."
        except Exception as exc:
            error_message = str(exc)
        finally:
            with _warmup_lock:
                WARMUP_STATE["in_progress"] = False
                WARMUP_STATE["ready"] = ready
                WARMUP_STATE["error"] = error_message


    def ensure_agent_warmup() -> None:
        with _warmup_lock:
            if WARMUP_STATE["in_progress"] or WARMUP_STATE["ready"]:
                return
            WARMUP_STATE["in_progress"] = True
            WARMUP_STATE["error"] = None
        threading.Thread(target=_warm_agent_models, daemon=True).start()


    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )


    @app.on_event("startup")
    async def startup_event() -> None:
        ensure_agent_warmup()


    @app.get("/", response_class=HTMLResponse)
    async def index() -> str:
        return HTML_PAGE


    @app.get("/health")
    async def health() -> dict:
        return {"status": "ok", "warmup": dict(WARMUP_STATE)}


    @app.post("/warmup")
    async def warmup_endpoint() -> dict:
        ensure_agent_warmup()
        return {"ok": True, "warmup": dict(WARMUP_STATE)}


    @app.post("/fetch")
    async def fetch_endpoint(request: FetchRequest) -> dict:
        clean_topics = [(topic or "").strip() for topic in request.topics if (topic or "").strip()][:3]
        if not clean_topics:
            return {
                "articles": [],
                "briefing": "",
                "topics": [],
                "reasoning_log": {},
                "topic_briefings": {},
            }
        ensure_agent_warmup()
        return await run_in_threadpool(run_agent_for_topics, clean_topics)


    @app.post("/translate")
    async def translate_endpoint(request: TranslateRequest) -> dict:
        if (request.language or "English").strip().lower() == "english":
            return {"articles": request.articles}
        translated = await run_in_threadpool(translate_articles, request.articles, request.language)
        return {"articles": translated}


    @app.post("/chat")
    async def chat_endpoint(request: ChatRequest) -> dict:
        return await run_in_threadpool(
            generate_chatbot_response,
            message=request.message,
            history=request.history,
            last_topic=request.last_topic,
            articles=request.articles,
        )


    @app.post("/visuals")
    async def visuals_endpoint(request: VisualRequest) -> dict:
        return await run_in_threadpool(build_visual_payload, request.articles)


    if __name__ == "__main__":
        import uvicorn

        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
    '''
).strip("\n")


MODULES = {
    "fetch_news.py": FETCH_NEWS,
    "sentiment.py": SENTIMENT,
    "nlp_pipeline.py": NLP_PIPELINE,
    "translator.py": TRANSLATOR,
    "visualizations.py": VISUALIZATIONS,
    "agent.py": AGENT,
    "chatbot.py": CHATBOT,
    "templates.py": TEMPLATES,
    "main.py": MAIN,
}


for filename, source in MODULES.items():
    compile(source, filename, "exec")


cells = [
    md(
        """
        # VeritasAI — Truth-Driven News Intelligence

        VeritasAI is a real-time AI-powered news aggregator agent built for the
        Application Developer RA position at Rutgers MPI. This notebook contains
        the complete project in a single Colab file — from data fetching all the
        way to a fully custom web interface accessible from any browser.

        The core idea is simple. Most news aggregators are pipelines. They follow
        the same fixed steps every time regardless of what they find. VeritasAI is
        built around a genuine AI agent loop using Google's flan-t5-base open-source
        language model. After every action, the agent observes its results, reasons
        about quality, and decides what to do next. The sequence of steps adapts to
        each topic individually.

        ---

        ## How to Run

        1. Run Cell 1 (this cell is just text, skip to Cell 2)
        2. Run Cell 2 to install all dependencies — takes 2 to 3 minutes, run once only
        3. Run all remaining cells from top to bottom in order
        4. Run the final launch cell — it will print a public URL ending in trycloudflare.com
        5. Open that URL in your browser and start searching

        No API keys, no accounts, and no tokens are required.

        ---

        ## Features

        ### Core Requirements
        - Three topic inputs on the frontend search page
        - AI agent fetches the 10 most recent articles per topic from Google News RSS
        - VADER sentiment classification per headline (Positive, Negative, Neutral)
        - Articles sorted by publication date descending, most recent first
        - All headlines displayed as clickable links with source and date metadata

        ### AI Agent (flan-t5-base)
        - Google flan-t5-base open-source language model as the reasoning engine
        - Six tools in the tool registry: search_news, assess_quality, refine_query,
          broaden_query, analyze_sentiment, summarize
        - Observe-reason-act loop running up to 3 retry attempts per topic
        - Topic specificity assessed by spaCy NER before the first search
        - Quality assessed by checking article count and headline relevance
        - Full reasoning log shown in the sidebar after each search

        ### Text Visualizations (Voyant-inspired)
        - Word cloud with circular mask and custom color palette
        - Sentiment distribution donut chart
        - Top 15 keyword frequency bar chart
        - Sentiment score scatter plot over publication time

        ### Multilingual Translation
        - Helsinki-NLP OPUS-MT open-source models from HuggingFace
        - Supports Spanish, Hindi, French, and German
        - Language toggle in the frontend, models cache after first load

        ### VeritasBot (Optional Chat)
        - Responds to natural language queries like "Find news on Intel stock price"
        - Returns 1 to 3 clickable article URLs plus a courtesy comment
        - Six enhancements: spaCy NER query understanding, multi-turn memory,
          sentiment-aware response tone, follow-up suggestion chips, TextRank
          briefing mode, and sentiment percentage commentary on every response

        ---

        ## Tech Stack

        | Tool | Purpose |
        |---|---|
        | flan-t5-base (HuggingFace) | Open-source LLM for agent reasoning |
        | feedparser | Google News RSS parsing, no API key needed |
        | VADER (vaderSentiment) | Headline sentiment classification |
        | spaCy en_core_web_sm | Named entity recognition |
        | sumy TextRank | Extractive summarization |
        | Helsinki-NLP OPUS-MT | Open-source neural machine translation |
        | wordcloud + numpy | Word cloud with circular mask |
        | Plotly | Interactive charts |
        | python-dateutil | Robust date string parsing |
        | FastAPI + uvicorn | Backend web framework |
        | Cloudflare Tunnel | Free public URL, no account needed |

        ---

        ## AI Usage Declaration

        This notebook was developed with assistance from an AI coding assistant
        during development only. The AI was not integrated into the running
        application at any point. All LLMs used inside the app at runtime
        (flan-t5-base and Helsinki-NLP OPUS-MT) are fully open-source and
        publicly available on HuggingFace.

        The AI assistant helped with: translation pipeline integration, FastAPI
        routing structure, and debugging library compatibility issues. All core
        design decisions including the agent architecture, tool registry, chatbot
        enhancement logic, and frontend layout were made independently.

        ---

        ## References

        All references are listed in the final cell of this notebook.
        """
    ),
    md(
        """
        ## Step 1 — Install All Runtime Dependencies

        This cell installs every Python library the project needs, downloads the
        spaCy English NER model, fetches the NLTK tokenizer data required by sumy
        TextRank, and downloads the cloudflared binary that creates the public URL.

        Run this cell first and wait for it to finish before running any other cell.
        In a fresh Colab session this takes about 2 to 3 minutes depending on
        network speed.

        Libraries installed:
        - fastapi, uvicorn: web framework and server
        - feedparser: RSS feed parsing
        - vaderSentiment: headline sentiment analysis
        - python-dateutil: robust date parsing
        - spacy: named entity recognition
        - sumy: TextRank extractive summarization
        - wordcloud, matplotlib, numpy: visualization support
        - plotly: interactive charts
        - transformers, sentencepiece, sacremoses, accelerate: HuggingFace model loading
        - nltk: tokenizer data for sumy
        - torch (CPU build): required by transformers for model inference
        """
    ),
    code(
        r'''
        import os
        import stat
        import subprocess
        import sys
        from pathlib import Path

        PACKAGES = [
            "fastapi",
            "uvicorn",
            "feedparser",
            "vaderSentiment",
            "python-dateutil",
            "spacy",
            "sumy",
            "wordcloud",
            "plotly",
            "transformers",
            "sentencepiece",
            "sacremoses",
            "accelerate",
            "nltk",
            "matplotlib",
            "numpy",
            "torch",
        ]

        subprocess.run([sys.executable, "-m", "pip", "install", "-q", *PACKAGES], check=True)
        subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm", "-q"], check=True)

        import nltk

        for resource_name in ("punkt", "punkt_tab"):
            try:
                nltk.download(resource_name, quiet=True)
            except Exception:
                pass

        CLOUDFLARED_URL = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"
        cloudflared_path = Path("/content/cloudflared")

        def download_cloudflared(target: Path) -> None:
            commands = [
                [
                    "curl",
                    "-L",
                    "--fail",
                    "--retry",
                    "4",
                    "--retry-all-errors",
                    "--connect-timeout",
                    "20",
                    CLOUDFLARED_URL,
                    "-o",
                    str(target),
                ],
                [
                    "wget",
                    "-q",
                    "--tries=4",
                    "--timeout=20",
                    CLOUDFLARED_URL,
                    "-O",
                    str(target),
                ],
            ]
            errors = []

            for command in commands:
                try:
                    if target.exists():
                        target.unlink()
                    subprocess.run(command, check=True)
                    if target.exists() and target.stat().st_size > 0:
                        target.chmod(target.stat().st_mode | stat.S_IEXEC)
                        return
                    errors.append(f"{command[0]} produced an empty file")
                except Exception as exc:
                    errors.append(f"{command[0]} failed: {exc}")

            raise RuntimeError(
                "Cloudflared download failed after retrying with curl and wget. "
                + " | ".join(errors)
            )

        if not cloudflared_path.exists() or cloudflared_path.stat().st_size == 0:
            download_cloudflared(cloudflared_path)

        print("Setup complete. Runtime dependencies and cloudflared are ready.")
        '''
    ),
    md(
        """
        ## Step 2 — News Fetching Module

        This module is the first tool in the agent's tool registry. Every time the
        agent decides to fetch news it calls the functions defined here.

        The fetcher uses Google News RSS because it is free, requires no API key,
        returns real-time results for any search query, and includes publication
        timestamps which are needed for sorting. The feedparser library parses the
        RSS feed into Python objects.

        Each article comes back as a dictionary with these fields:
        - headline: cleaned title with source suffix removed
        - translated_headline: initially same as headline, updated by the translator
        - link: direct URL to the full article
        - source: publisher name extracted from the RSS entry
        - published: raw date string from the RSS feed
        - topic: which search topic this article belongs to

        The fetch_all_topics function loops over up to 3 topics and combines results
        into one flat list for the agent to process.
        """
    ),
    code(f"%%writefile /content/fetch_news.py\n{FETCH_NEWS}"),
    md(
        """
        ## Step 3 — Sentiment and Date Processing Module

        This module does two things to every article. First it parses the raw date
        string into a proper datetime object so articles can be sorted correctly.
        Second it runs every headline through VADER sentiment analysis.

        VADER stands for Valence Aware Dictionary and sEntiment Reasoner. It was
        built specifically for short social media and news-style text, which makes
        it more accurate on headlines than general-purpose models. It handles
        negation, capitalization, and punctuation automatically.

        VADER returns a compound score between -1.0 and +1.0. We map this to three
        labels using the thresholds recommended in the original research paper:
        - 0.05 and above: Positive
        - -0.05 and below: Negative
        - Between -0.05 and 0.05: Neutral

        The process_articles function also removes duplicate headlines and sorts
        everything by date descending so the most recent article always appears first,
        satisfying the assignment requirement directly.
        """
    ),
    code(f"%%writefile /content/sentiment.py\n{SENTIMENT}"),
    md(
        """
        ## Step 4 — NLP Utility Module

        This module handles two NLP tasks that are used in different parts of
        the project.

        The first is Named Entity Recognition using spaCy. When a user types
        something into VeritasBot like "what is happening with Apple?" the bot
        needs to figure out that Apple is the topic to search. spaCy's NER model
        identifies real-world entities like organizations, people, and locations
        regardless of how the sentence is phrased.

        The same NER logic is used by the agent to assess whether a topic is
        specific enough to search directly or too vague and needs expansion first.

        The second task is TextRank summarization via the sumy library. TextRank
        is a graph-based algorithm that identifies the most representative sentences
        in a body of text by measuring how similar each sentence is to all the
        others. The most connected sentences win. This is the same technique used
        by Google News Briefings and it runs entirely locally with no additional
        model download needed.

        TextRank powers two features: the News Brief card that appears at the top
        of results after each fetch, and the briefing mode in VeritasBot when the
        user asks for a summary.
        """
    ),
    code(f"%%writefile /content/nlp_pipeline.py\n{NLP_PIPELINE}"),
    md(
        """
        ## Step 5 — Multilingual Translation Module

        This module adds multilingual support to VeritasAI. When the user selects
        a language from the dropdown, all fetched headlines translate instantly to
        that language without re-fetching the news.

        Translation uses Helsinki-NLP OPUS-MT models from HuggingFace. These are
        open-source neural machine translation models trained on millions of
        sentence pairs. There is a separate model for each language direction —
        English to Spanish, English to Hindi, English to French, and English to
        German. Each model is around 300MB.

        To avoid loading all models at startup, each model loads only when the user
        selects that language for the first time. After that it is cached using
        Python's lru_cache so subsequent translations for the same language are
        near-instant. The first translation for a new language takes 20 to 40
        seconds while the model downloads.

        All models run locally inside Colab. No data is sent to any external API
        and no authentication is required.
        """
    ),
    code(f"%%writefile /content/translator.py\n{TRANSLATOR}"),
    md(
        """
        ## Step 6 — Visualization Module

        This module generates four visual elements that appear in the Insights
        section of the frontend. Each visualization answers a specific question
        about the fetched article set.

        Word Cloud: What words dominate the headlines right now? Combines all
        headlines, filters stopwords, and renders a circular word cloud where
        larger words appear more frequently. Uses a custom color function with
        near-black, grey, and gold shades. The circular shape uses a numpy mask.

        Sentiment Pie Chart: Is overall coverage positive, negative, or neutral?
        An interactive donut chart showing proportions across all fetched articles.

        Keyword Bar Chart: Which specific terms appear most often? The top 15
        most frequent non-stopword terms ranked by count.

        Sentiment Scatter Plot: Has coverage sentiment shifted over time? Each
        article is plotted as a dot with publication time on the x-axis and VADER
        compound score on the y-axis. Dashed threshold lines at +0.05 and -0.05
        show the positive and negative boundaries.

        All charts are built with Plotly and sent to the frontend as JSON. The
        browser renders them using the Plotly CDN with full interactivity.
        """
    ),
    code(f"%%writefile /content/visualizations.py\n{VISUALIZATIONS}"),
    md(
        """
        ## Step 7 — VeritasAgent (The AI Brain)

        This is the module that makes VeritasAI genuinely different from a standard
        news aggregator pipeline. A pipeline always follows the same steps in the
        same order. VeritasAgent does not.

        The agent uses Google's flan-t5-base open-source language model as its
        reasoning engine. flan-t5-base is an instruction-tuned sequence-to-sequence
        model trained to follow natural language prompts. It runs on CPU inside
        Colab without requiring a GPU.

        The observe-reason-act loop works like this for each topic:

        1. OBSERVE: The agent reads the topic and uses spaCy to assess how
           specific it is (specific, vague, or person entity)

        2. REASON: flan-t5 decides whether to search directly or expand the
           query first. Specific topics like company names search directly.
           Vague topics get expanded.

        3. ACT: The agent calls the search tool and fetches articles.

        4. OBSERVE: The agent reads the results. How many came back? Are the
           headlines actually about the topic?

        5. REASON: flan-t5 evaluates quality and decides to accept, broaden,
           or refine the query. Rule-based heuristics provide a fallback if
           flan-t5 is unavailable.

        6. ACT: If not accepted, the query is rewritten and the loop retries.
           Maximum 3 attempts before accepting whatever is available.

        After the loop, VADER sentiment is applied and TextRank generates a
        briefing. The full reasoning log is returned to the frontend and shown
        in the sidebar so the user can see every decision the agent made.
        """
    ),
    code(f"%%writefile /content/agent.py\n{AGENT}"),
    md(
        """
        ## Step 8 — VeritasBot Chatbot Module

        VeritasBot is the conversational layer that sits on top of everything
        the agent has already built. Once news is loaded the user can have a
        natural conversation about it or ask for new searches.

        Six enhancements are built on top of a base news search chatbot:

        Enhancement 1: Natural language query understanding via spaCy NER. The
        user can type anything and the bot extracts the topic. "What is happening
        with Apple lately?" works the same as "Find news on Apple."

        Enhancement 2: Multi-turn memory. The bot tracks the last topic so
        follow-up messages like "what about their stock price?" resolve correctly
        against the previous context.

        Enhancement 3: Sentiment-aware response tone. The bot checks the
        sentiment breakdown of what it finds and adjusts its opening sentence
        accordingly. Mostly negative coverage gets a different opener than
        mostly positive.

        Enhancement 4: Suggested follow-up chips. After every response the bot
        generates 2 to 3 clickable topic buttons from entities in the fetched
        headlines. The user clicks a chip and it auto-sends as the next message.

        Enhancement 5: Briefing mode. When the user asks for a briefing or
        summary, TextRank runs and returns a 2 to 3 sentence digest.

        Enhancement 6: Sentiment percentage commentary. Every response ends
        with an exact breakdown like 60% Positive, 30% Negative, 10% Neutral.

        The chatbot returns structured data with article objects so the frontend
        can render proper clickable cards with colored borders, not plain URLs.
        """
    ),
    code(f"%%writefile /content/chatbot.py\n{CHATBOT}"),
    md(
        """
        ## Step 9 — Frontend Template

        This cell writes the complete HTML, CSS, and JavaScript frontend to a
        file called templates.py. The entire frontend is embedded as a Python
        raw string so everything stays inside one Colab file.

        The frontend is a custom news website design with:
        - Clean white background and bold typography
        - Top navbar with centered logo and category navigation
        - Search section with three topic inputs and a language dropdown
        - Briefing card that appears after the first fetch
        - Featured hero article on the left with large bold headline
        - Secondary articles listed on the right with thumbnail placeholders
        - Insights section with word cloud and three Plotly charts
        - VeritasBot chat panel with message bubbles and suggestion chips
        - Agent reasoning log showing every step the agent took

        All state is managed in JavaScript variables. The frontend calls the
        FastAPI endpoints using the browser's built-in fetch API with no
        external JavaScript framework needed.
        """
    ),
    code(f"%%writefile /content/templates.py\n{TEMPLATES}"),
    md(
        """
        ## Step 10 — FastAPI Application

        This cell writes the FastAPI backend that connects everything together.
        FastAPI handles all HTTP requests from the browser and routes them to
        the correct Python module.

        Five endpoints are exposed:

        GET / serves the full HTML page from templates.py

        POST /fetch runs the VeritasAgent for up to 3 topics and returns
        the processed articles, briefing text, and reasoning log

        POST /translate runs the Helsinki-NLP translation pipeline and
        returns articles with translated_headline added to each one

        POST /chat runs VeritasBot and returns a structured response with
        article links and suggestion chips

        POST /visuals generates the word cloud and three Plotly charts and
        returns them as base64 image data and JSON

        CORS middleware is added so the frontend can call the API from the
        Cloudflare tunnel domain without cross-origin errors.
        """
    ),
    code(f"%%writefile /content/main.py\n{MAIN}"),
    md(
        """
        ## Step 11 — Syntax Check

        This cell runs a quick compile check on every generated Python file
        before launch. If any file contains a syntax error this cell will
        fail and print exactly which file and which line caused the problem.

        This saves time compared to discovering syntax errors after the server
        has already started, where the error message is harder to read.

        If all files pass the check you will see "All generated modules compiled
        successfully" and can proceed to the launch cell.
        """
    ),
    code(
        r'''
        import py_compile

        module_paths = [
            "/content/fetch_news.py",
            "/content/sentiment.py",
            "/content/nlp_pipeline.py",
            "/content/translator.py",
            "/content/visualizations.py",
            "/content/agent.py",
            "/content/chatbot.py",
            "/content/templates.py",
            "/content/main.py",
        ]

        for module_path in module_paths:
            py_compile.compile(module_path, doraise=True)

        print("All generated modules compiled successfully.")
        '''
    ),
    md(
        """
        ## Step 12 — Launch VeritasAI

        This is the final cell. Running it starts the FastAPI server on port 8000
        inside the Colab environment, then creates a public HTTPS URL using
        Cloudflare Tunnel so the app can be opened from any browser anywhere.

        The cell shuts down any previous server or tunnel from earlier in the
        session before starting fresh, so it is safe to rerun.

        After running this cell:
        1. Wait about 15 to 20 seconds for the tunnel to establish
        2. A URL ending in trycloudflare.com will print to the output
        3. Copy that URL and open it in any browser
        4. Enter up to three topics and click Fetch News
        5. The agent will run and results will appear in seconds

        Important notes:
        - The URL is only active while this Colab session is running
        - Always use the newest URL printed by this cell; older trycloudflare URLs expire and return DNS errors
        - If you ever see DNS_PROBE_FINISHED_NXDOMAIN, rerun only this launch cell and open the new URL it prints
        - If Colab disconnects, rerun all cells from the top and run this cell again
        - The launch cell now starts warming the FLAN agent before you open the public URL
        - The very first fetch can still take longer than later ones if the warm-up is still finishing
        - The first translation for each language takes 20 to 40 seconds to download the model
        - Every action after those first loads is much faster

        Before submitting, set Colab sharing to "Anyone with the link" using
        the Share button in the top right corner.
        """
    ),
    code(
        r'''
        import json
        import os
        import re
        import subprocess
        import time
        from pathlib import Path
        from urllib.error import HTTPError, URLError
        from urllib.request import urlopen

        os.chdir("/content")

        def tail_text(path: str, lines: int = 20) -> str:
            content = Path(path).read_text(errors="ignore").splitlines()
            return "\n".join(content[-lines:])

        for process_name in ("uvicorn_process", "cloudflared_process"):
            process = globals().get(process_name)
            if process and process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()

        for artifact_path in (
            "/content/uvicorn.log",
            "/content/cloudflared.log",
            "/content/veritas_public_url.txt",
        ):
            try:
                Path(artifact_path).unlink()
            except FileNotFoundError:
                pass

        uvicorn_log = open("/content/uvicorn.log", "w", buffering=1)
        cloudflared_log = open("/content/cloudflared.log", "w", buffering=1)

        uvicorn_process = subprocess.Popen(
            ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"],
            stdout=uvicorn_log,
            stderr=subprocess.STDOUT,
        )

        backend_ready = False
        for _ in range(45):
            if uvicorn_process.poll() is not None:
                break
            try:
                with urlopen("http://127.0.0.1:8000/health", timeout=2) as response:
                    if getattr(response, "status", 200) == 200:
                        backend_ready = True
                        break
            except Exception:
                time.sleep(2)

        print("FastAPI log file: /content/uvicorn.log")
        print("Cloudflare log file: /content/cloudflared.log")

        if not backend_ready:
            print("FastAPI did not become healthy. Check /content/uvicorn.log.")
            print(tail_text("/content/uvicorn.log"))
            raise RuntimeError("Backend startup failed before Cloudflare tunnel launch.")

        try:
            with urlopen(
                "http://127.0.0.1:8000/warmup",
                data=b"{}",
                timeout=4,
            ) as response:
                warmup_payload = json.loads(response.read().decode("utf-8"))
            warmup_state = warmup_payload.get("warmup", {})
            if warmup_state.get("ready"):
                print("Agent warm-up is already ready.")
            else:
                print("Agent warm-up started in the background.")
        except Exception:
            print("Agent warm-up trigger could not be confirmed, but the app will still start.")

        cloudflared_process = subprocess.Popen(
            ["/content/cloudflared", "tunnel", "--url", "http://127.0.0.1:8000", "--no-autoupdate"],
            stdout=cloudflared_log,
            stderr=subprocess.STDOUT,
        )

        public_url = None
        for _ in range(60):
            if cloudflared_process.poll() is not None:
                break
            log_text = Path("/content/cloudflared.log").read_text(errors="ignore")
            match = re.search(r"https://[-a-zA-Z0-9]+\.trycloudflare\.com", log_text)
            if match:
                candidate_url = match.group(0)
                try:
                    with urlopen(f"{candidate_url}/health", timeout=5) as response:
                        if getattr(response, "status", 200) == 200:
                            public_url = candidate_url
                            break
                except (HTTPError, URLError, TimeoutError, OSError):
                    pass
            time.sleep(2)

        if public_url:
            Path("/content/veritas_public_url.txt").write_text(public_url + "\n")
            print("Public frontend URL (use only this newest URL):", public_url)
            print("Saved URL file: /content/veritas_public_url.txt")
        else:
            print("Cloudflare did not produce a verified public URL yet.")
            print("If you rerun this cell, only the newest URL remains valid.")
            print("Recent cloudflared log lines:")
            print(tail_text("/content/cloudflared.log"))
        '''
    ),
    md(
        """
        ## References

        All libraries, tools, and external resources used in this project:

        | Resource | Purpose | Link |
        |---|---|---|
        | Google News RSS | Live news data source | https://news.google.com/rss |
        | feedparser | RSS feed parsing | https://feedparser.readthedocs.io |
        | vaderSentiment | Headline sentiment analysis | https://github.com/cjhutto/vaderSentiment |
        | spaCy en_core_web_sm | Named entity recognition | https://spacy.io |
        | sumy TextRank | Extractive summarization | https://github.com/miso-belica/sumy |
        | Voyant Tools | Visualization inspiration | https://voyant-tools.org |
        | wordcloud | Word cloud generation | https://amueller.github.io/word_cloud |
        | numpy | Circular mask for word cloud | https://numpy.org |
        | Plotly | Interactive charts | https://plotly.com/python |
        | python-dateutil | Robust date parsing | https://dateutil.readthedocs.io |
        | HuggingFace Transformers | Model loading framework | https://huggingface.co/docs/transformers |
        | google/flan-t5-base | Open-source reasoning LLM | https://huggingface.co/google/flan-t5-base |
        | Helsinki-NLP OPUS-MT | Open-source translation models | https://huggingface.co/Helsinki-NLP |
        | FastAPI | Backend web framework | https://fastapi.tiangolo.com |
        | uvicorn | ASGI server | https://www.uvicorn.org |
        | Cloudflare Tunnel | Free public HTTPS URL | https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/do-more-with-tunnels/trycloudflare |
        | Inter font | Typography | https://fonts.google.com/specimen/Inter |
        | Plotly CDN | Frontend chart rendering | https://cdn.plot.ly/plotly-latest.min.js |
        """
    ),
]


notebook = {
    "cells": cells,
    "metadata": {
        "colab": {
            "name": NOTEBOOK_NAME,
            "provenance": [],
            "include_colab_link": True,
        },
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "name": "python",
            "version": "3.10",
        },
    },
    "nbformat": 4,
    "nbformat_minor": 0,
}


output_path = Path(NOTEBOOK_NAME)
output_path.write_text(json.dumps(notebook, indent=2), encoding="utf-8")
print(f"Wrote {output_path.resolve()}")
