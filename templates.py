HTML_PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
  <meta http-equiv="Pragma" content="no-cache" />
  <meta http-equiv="Expires" content="0" />
  <title>VeritasAI</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><circle cx=%2250%22 cy=%2250%22 r=%2248%22 fill=%22%232D8A70%22/><text y=%22.9em%22 x=%2250%%22 font-size=%2270%22 text-anchor=%22middle%22 fill=%22white%22 font-family=%22serif%22 font-weight=%22bold%22>V</text></svg>"> 
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@1,500;1,600&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@800&family=Playfair+Display:ital,wght@1,900&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Newsreader:opsz,wght@6..72,600;6..72,700;6..72,800&display=swap" rel="stylesheet" />
  <script>
    (function () {
      function keepWarm() {
        fetch("/", { cache: "no-store" }).catch(function () {});
      }
      keepWarm();
      window.__veritasKeepWarm = window.setInterval(keepWarm, 45000);
    })();
  </script>
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <style>
    :root {
      color-scheme: light;
      --bg-color: #FDFCF8;
      --text-color: #1A1A1A;
      --card-shadow: rgba(0, 0, 0, 0.04);
      --card-bg: #FFFFFF;
      --bg: var(--bg-color);
      --surface: var(--card-bg);
      --surface-soft: #F4F0E7;
      --surface-muted: #ECE7DB;
      --text: var(--text-color);
      --muted: #566257;
      --muted-soft: #768274;
      --border: rgba(23, 33, 25, 0.10);
      --accent: #215E46;
      --accent-bright: #2D8A70;
      --accent-dark: #164633;
      --accent-soft: #E1EEE7;
      --positive-bg: #ECF8F1;
      --positive-text: #20643F;
      --positive-border: #BCDCC8;
      --negative-bg: #FBEFED;
      --negative-text: #A63B32;
      --negative-border: #E8C0BA;
      --neutral-bg: #F1F0EC;
      --neutral-text: #6A726C;
      --neutral-border: #DFE2DC;
      --shadow-sm: 0 16px 40px var(--card-shadow);
      --shadow-lg: 0 30px 72px rgba(0, 0, 0, 0.08);
      --page-radial: rgba(45, 138, 112, 0.06);
      --page-bg-start: #FDFCF8;
      --page-bg-end: #FDFCF8;
      --hero-radial-strong: rgba(45, 138, 112, 0.10);
      --hero-radial-soft: rgba(45, 138, 112, 0.06);
      --hero-bg-start: #FDFCF8;
      --hero-bg-end: #FDFCF8;
      --hero-terminal-bg: linear-gradient(180deg, rgba(255, 255, 255, 0.9), rgba(252, 249, 243, 0.84));
      --hero-terminal-accent: rgba(45, 138, 112, 0.08);
      --blank-card-bg: #FFFFFF;
      --blank-card-line: #EFF2EE;
      --blank-chip-bg: #F3F5F3;
      --blank-card-box-bg: #FAFBFA;
      --ghost-bg: rgba(255, 255, 255, 0.76);
      --ghost-hover-bg: #FFFFFF;
      --ticker-badge-bg: #1A1A1A;
      --ticker-badge-text: #FFFFFF;
      --warm-status: #B45309;
      --chart-grid: rgba(0, 0, 0, 0.10);
      --chart-zero: rgba(0, 0, 0, 0.16);
      --chart-band: rgba(45, 138, 112, 0.10);
      --chart-marker: rgba(33, 94, 70, 0.72);
      --chart-marker-line: rgba(255, 255, 255, 0.92);
      --chart-legend: #1A1A1A;
      --max-width: 1440px;
    }

    * {
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
    }

    body[data-theme="dark"] {
      color-scheme: dark;
      --bg-color: #121212;
      --text-color: #F5F5F5;
      --card-shadow: rgba(0, 0, 0, 0.4);
      --card-bg: #1E1E1E;
      --bg: var(--bg-color);
      --surface: var(--card-bg);
      --surface-soft: #1A1A1A;
      --surface-muted: #222222;
      --text: var(--text-color);
      --muted: #B5C3B8;
      --muted-soft: #8F9E92;
      --border: rgba(218, 232, 221, 0.10);
      --accent: #66B397;
      --accent-bright: #2D8A70;
      --accent-dark: #4B9A7E;
      --accent-soft: rgba(45, 138, 112, 0.16);
      --positive-bg: rgba(45, 138, 112, 0.16);
      --positive-text: #C5F1D5;
      --positive-border: rgba(103, 183, 133, 0.28);
      --negative-bg: rgba(169, 68, 66, 0.16);
      --negative-text: #F7C4C3;
      --negative-border: rgba(169, 68, 66, 0.26);
      --neutral-bg: rgba(112, 128, 144, 0.14);
      --neutral-text: #D4DBE2;
      --neutral-border: rgba(112, 128, 144, 0.22);
      --shadow-sm: 0 16px 40px var(--card-shadow);
      --shadow-lg: 0 30px 72px rgba(0, 0, 0, 0.55);
      --page-radial: rgba(45, 138, 112, 0.12);
      --page-bg-start: #121212;
      --page-bg-end: #171717;
      --hero-radial-strong: rgba(45, 138, 112, 0.16);
      --hero-radial-soft: rgba(45, 138, 112, 0.08);
      --hero-bg-start: #121212;
      --hero-bg-end: #171717;
      --hero-terminal-bg: linear-gradient(180deg, rgba(24, 24, 24, 0.94), rgba(18, 18, 18, 0.92));
      --hero-terminal-accent: rgba(45, 138, 112, 0.12);
      --blank-card-bg: #1A1A1A;
      --blank-card-line: rgba(219, 231, 223, 0.10);
      --blank-chip-bg: rgba(219, 231, 223, 0.08);
      --blank-card-box-bg: #222222;
      --ghost-bg: rgba(24, 24, 24, 0.76);
      --ghost-hover-bg: rgba(31, 31, 31, 0.94);
      --ticker-badge-bg: #F1F5F1;
      --ticker-badge-text: #132018;
      --warm-status: #EAB308;
      --chart-grid: rgba(219, 231, 223, 0.10);
      --chart-zero: rgba(219, 231, 223, 0.18);
      --chart-band: rgba(45, 138, 112, 0.18);
      --chart-marker: rgba(102, 179, 151, 0.76);
      --chart-marker-line: rgba(15, 21, 17, 0.92);
      --chart-legend: #D8E0DA;
    }

    body {
      margin: 0;
      background:
        radial-gradient(circle at top left, var(--page-radial), transparent 24%),
        linear-gradient(180deg, var(--page-bg-start) 0%, var(--page-bg-end) 100%);
      color: var(--text);
      font-family: "Inter", sans-serif;
      -webkit-font-smoothing: antialiased;
      text-rendering: optimizeLegibility;
      transition: background 0.28s ease, color 0.28s ease;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    button,
    input,
    select {
      font: inherit;
    }

    button {
      cursor: pointer;
    }

    .shell {
      max-width: var(--max-width);
      margin: 0 auto;
      padding: 0 28px 40px;
    }

    .surface {
      background-color: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 1.5rem;
      box-shadow: var(--shadow-sm);
      backdrop-filter: blur(18px);
    }

    .interactive {
      transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease, background-color 0.22s ease;
    }

    .interactive:hover {
      transform: translateY(-4px);
      box-shadow: var(--shadow-lg);
    }

    .hero {
      position: relative;
      overflow: hidden;
      padding: 60px 28px;
      background:
        radial-gradient(circle at top right, var(--hero-radial-strong), transparent 30%),
        radial-gradient(circle at left center, var(--hero-radial-soft), transparent 28%),
        linear-gradient(180deg, var(--hero-bg-start) 0%, var(--hero-bg-end) 100%);
      border-bottom: 1px solid rgba(23, 33, 25, 0.08);
    }

    .hero-inner {
      position: relative;
      z-index: 2;
      max-width: 1040px;
      margin: 0 auto;
      text-align: center;
    }

    .theme-toggle {
      min-height: 48px;
      padding: 0 14px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: var(--ghost-bg);
      color: var(--muted);
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.02em;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      backdrop-filter: blur(10px);
      transition: transform 0.2s ease, border-color 0.2s ease, background-color 0.2s ease, color 0.2s ease;
    }

    .theme-toggle:hover {
      transform: translateY(-1px);
      color: var(--accent);
      border-color: rgba(33, 94, 70, 0.24);
      background: var(--ghost-hover-bg);
    }

    .logo-wrapper {
      display: flex;
      align-items: baseline;
      justify-content: center;
      gap: 0.08rem;
      font-size: clamp(3rem, 8vw, 5.2rem);
      line-height: 1;
    }

    .veritas-serif {
      font-family: "Playfair Display", serif;
      font-style: italic;
      font-weight: 900;
      color: var(--text);
      position: relative;
      letter-spacing: -0.02em;
      line-height: 0.92;
    }

    .veritas-i {
      position: relative;
      display: inline-block;
    }

    .veritas-i::after {
      content: "";
      position: absolute;
      left: 50%;
      top: -4px;
      transform: translateX(-50%);
      width: 8px;
      height: 8px;
      background: #2D8A70;
      border-radius: 50%;
      box-shadow:
        0 0 0 1px rgba(255, 255, 255, 0.45),
        0 0 10px rgba(45, 138, 112, 0.4),
        0 0 20px rgba(45, 138, 112, 0.16);
    }

    .ai-sans {
      font-family: "Inter", sans-serif;
      font-weight: 800;
      color: var(--text);
      font-size: 0.8em;
      letter-spacing: 0.05em;
      margin-left: 0.08em;
      text-transform: uppercase;
    }

    .hero-tagline {
      margin: 12px 0 0;
      color: var(--accent);
      font-size: 0.78rem;
      font-weight: 800;
      letter-spacing: 0.28em;
      text-transform: uppercase;
      animation: trackingInExpand 0.95s cubic-bezier(0.2, 0.8, 0.2, 1) both 0.12s;
    }

    .hero-copy {
      max-width: 780px;
      margin: 0.9rem auto 0;
      color: var(--muted);
      font-size: 1rem;
      line-height: 1.86;
    }

    .hero-actions {
      display: flex;
      align-items: center;
      justify-content: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 10px;
    }

    .hero-actions .control {
      width: auto;
      min-width: 220px;
      flex: 0 1 220px;
      box-shadow: none;
    }

    .hero-actions > * {
      align-self: center;
    }

    .hero-visuals {
      position: relative;
      width: min(960px, 100%);
      min-height: 440px;
      margin: 28px auto 0;
      padding: 0.5rem 0 1rem;
      overflow: visible;
    }

    .blank-stack {
      position: relative;
      width: min(760px, 100%);
      height: 390px;
      margin: 0 auto;
      perspective: 1600px;
    }

    .synthesis-progress {
      position: absolute;
      inset: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1rem 0;
    }

    .synthesis-progress[hidden] {
      display: none;
    }

    .synthesis-progress-shell {
      width: min(560px, calc(100% - 32px));
      min-height: 240px;
      display: grid;
      align-content: center;
      justify-items: center;
      gap: 16px;
      padding: 2.2rem 2rem;
      border-radius: 1.75rem;
      border: 1px solid var(--border);
      background:
        var(--hero-terminal-bg),
        radial-gradient(circle at top right, var(--hero-terminal-accent), transparent 42%);
      box-shadow: 0 28px 62px var(--card-shadow);
      backdrop-filter: blur(14px);
    }

    .synthesis-progress-title {
      margin: 0;
      color: var(--text);
      font-size: 0.84rem;
      font-weight: 800;
      letter-spacing: 0.18em;
      text-transform: uppercase;
    }

    .synthesis-progress-track {
      position: relative;
      width: min(340px, 100%);
      height: 3px;
      border-radius: 999px;
      background: rgba(45, 138, 112, 0.16);
      overflow: hidden;
    }

    .synthesis-progress-track::after {
      content: "";
      position: absolute;
      top: 0;
      bottom: 0;
      width: 38%;
      border-radius: inherit;
      background: linear-gradient(90deg, rgba(45, 138, 112, 0), rgba(45, 138, 112, 0.95), rgba(45, 138, 112, 0));
      animation: synthesisPulse 1.9s ease-in-out infinite;
    }

    .synthesis-progress-message {
      max-width: 430px;
      margin: 0;
      min-height: 3.2rem;
      color: color-mix(in srgb, var(--accent) 82%, var(--text) 18%);
      font-family: "Montserrat", sans-serif;
      font-style: italic;
      font-size: 0.9rem;
      font-weight: 600;
      line-height: 1.7;
      letter-spacing: 0.01em;
      text-align: center;
      opacity: 0.88;
    }

    .synthesis-progress-cancel {
      min-height: 40px;
      padding: 0 14px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: transparent;
      color: var(--muted);
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.01em;
    }

    .synthesis-progress-cancel:hover {
      color: var(--accent);
      border-color: rgba(33, 94, 70, 0.26);
      background: var(--ghost-bg);
    }

    .blank-card {
      --card-transform: translateY(0);
      --card-transform-hidden: translateY(36px) scale(0.985);
      --card-transform-loaded: var(--card-transform);
      --card-transform-hover: var(--card-transform-loaded);
      --card-transform-focus: var(--card-transform-hover);
      position: absolute;
      width: min(430px, calc(100% - 40px));
      min-height: 245px;
      padding: 1.45rem;
      border-radius: 1.5rem;
      border: 1px solid rgba(23, 33, 25, 0.06);
      background: var(--blank-card-bg);
      box-shadow: 0 40px 80px var(--card-shadow);
      opacity: 0;
      transform: var(--card-transform-hidden);
      transform-origin: center center;
      transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: transform, opacity, box-shadow;
      overflow: hidden;
    }

    body.is-ready .blank-card {
      opacity: 1;
      transform: var(--card-transform);
    }

    .blank-card::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        linear-gradient(180deg, rgba(246, 247, 245, 0.28), rgba(255, 255, 255, 0)),
        radial-gradient(circle at top right, rgba(45, 138, 112, 0.06), transparent 35%);
      opacity: 1;
      transition: opacity 0.35s ease, background 0.35s ease;
      pointer-events: none;
    }

    .blank-card::after {
      content: "";
      position: absolute;
      left: 0;
      top: 0;
      width: 100%;
      height: 3px;
      background: #2D8A70;
      opacity: 0;
      transition: opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1);
      pointer-events: none;
    }

    .blank-card > * {
      position: relative;
      z-index: 1;
    }

    .blank-card--one {
      --card-transform: translateX(calc(-50% + 42px)) rotate(4deg) translateY(30px);
      --card-transform-hidden: translateX(calc(-50% + 42px)) rotate(4deg) translateY(58px) scale(0.985);
      --card-transform-loaded: translateX(calc(-50% + 62px)) rotate(4deg) translateY(20px);
      --card-transform-hover: translateX(calc(-50% + 320px)) rotate(2deg) translateY(4px);
      --card-transform-focus: translateX(calc(-50% + 320px)) rotate(2deg) translateY(4px) scale(1.05);
      left: 50%;
      bottom: 22px;
      z-index: 1;
      transition-delay: 0s;
    }

    .blank-card--two {
      --card-transform: translateX(calc(-50% - 42px)) rotate(-4deg) translateY(30px);
      --card-transform-hidden: translateX(calc(-50% - 42px)) rotate(-4deg) translateY(58px) scale(0.985);
      --card-transform-loaded: translateX(calc(-50% - 62px)) rotate(-4deg) translateY(20px);
      --card-transform-hover: translateX(calc(-50% - 320px)) rotate(-2deg) translateY(4px);
      --card-transform-focus: translateX(calc(-50% - 320px)) rotate(-2deg) translateY(4px) scale(1.05);
      left: 50%;
      bottom: 22px;
      z-index: 2;
      transition-delay: 0.15s;
    }

    .blank-card--three {
      --card-transform: translateX(-50%) translateY(0);
      --card-transform-hidden: translateX(-50%) translateY(44px) scale(0.985);
      --card-transform-loaded: translateX(-50%) translateY(-2px) scale(1);
      --card-transform-hover: translateX(-50%) translateY(-10px) scale(1);
      --card-transform-focus: translateX(-50%) translateY(-10px) scale(1.05);
      left: 50%;
      top: 0;
      width: min(500px, calc(100% - 28px));
      min-height: 300px;
      z-index: 3;
      transition-delay: 0.3s;
    }

    .blank-stack.is-loaded .blank-card {
      transform: var(--card-transform-loaded);
    }

    .blank-stack.is-loaded .blank-card--one {
      transition-delay: 0s;
    }

    .blank-stack.is-loaded .blank-card--two {
      transition-delay: 0.08s;
    }

    .blank-stack.is-loaded .blank-card--three {
      transition-delay: 0.16s;
    }

    .blank-stack.is-loaded .blank-card::before {
      opacity: 0.92;
    }

    @media (hover: hover) and (pointer: fine) {
      .blank-stack.is-loaded:hover .blank-card.is-live {
        transform: var(--card-transform-hover);
        opacity: 1;
        background: #FFFFFF;
        box-shadow: 0 34px 86px rgba(23, 33, 25, 0.18);
        transition-delay: 0s;
      }

      .blank-stack.is-loaded:hover .blank-card.is-live::before {
        opacity: 0.96;
      }

      .blank-stack.is-loaded:hover .blank-card--one.is-live,
      .blank-stack.is-loaded:hover .blank-card--two.is-live {
        box-shadow: 0 30px 76px rgba(23, 33, 25, 0.16);
      }

      .blank-stack.is-loaded:hover .blank-card--one.is-live::after,
      .blank-stack.is-loaded:hover .blank-card--two.is-live::after {
        opacity: 1;
      }

      .blank-stack.is-loaded:hover .blank-card--three.is-live {
        box-shadow: 0 40px 94px rgba(23, 33, 25, 0.20);
      }

      .blank-stack.is-loaded:hover:has(.blank-card.is-live:hover) .blank-card.is-live {
        opacity: 0.6;
      }

      .blank-stack.is-loaded:hover:has(.blank-card.is-live:hover) .blank-card.is-live:hover {
        opacity: 1;
        z-index: 999;
        transform: var(--card-transform-focus);
        box-shadow: 0 44px 108px rgba(23, 33, 25, 0.26);
      }

      body[data-theme="dark"] .blank-stack.is-loaded:hover .blank-card.is-live {
        background: #1E1E1E;
        box-shadow: 0 34px 88px rgba(0, 0, 0, 0.54);
      }

      body[data-theme="dark"] .blank-stack.is-loaded:hover .blank-card--one.is-live,
      body[data-theme="dark"] .blank-stack.is-loaded:hover .blank-card--two.is-live {
        box-shadow: 0 30px 80px rgba(0, 0, 0, 0.50);
      }

      body[data-theme="dark"] .blank-stack.is-loaded:hover .blank-card--three.is-live {
        box-shadow: 0 40px 96px rgba(0, 0, 0, 0.56);
      }

      body[data-theme="dark"] .blank-stack.is-loaded:hover:has(.blank-card.is-live:hover) .blank-card.is-live:hover {
        background: #1E1E1E;
        box-shadow:
          0 44px 110px rgba(0, 0, 0, 0.62),
          0 0 20px rgba(45, 138, 112, 0.14);
      }
    }

    @media (hover: none), (pointer: coarse) {
      .blank-card--one {
        --card-transform-loaded: translateX(calc(-50% + 88px)) rotate(4deg) translateY(18px);
      }

      .blank-card--two {
        --card-transform-loaded: translateX(calc(-50% - 88px)) rotate(-4deg) translateY(18px);
      }

      .blank-card--three {
        --card-transform-loaded: translateX(-50%) translateY(-6px) scale(1);
      }
    }

    .blank-card.is-live {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 1rem;
      background: #FFFFFF;
      border-color: rgba(23, 33, 25, 0.08);
      color: var(--text);
      box-shadow: 0 28px 70px rgba(23, 33, 25, 0.11);
    }

    .blank-card.is-live::before {
      background:
        radial-gradient(circle at top right, rgba(45, 138, 112, 0.10), transparent 34%),
        linear-gradient(180deg, rgba(255, 255, 255, 0.32), rgba(255, 255, 255, 0));
    }

    .hero-card-shell {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      min-height: 100%;
    }

    .hero-card-meta {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    .hero-card-kicker,
    .hero-card-stamp {
      display: inline-flex;
      align-items: center;
      min-height: 28px;
      padding: 0 10px;
      border-radius: 999px;
      border: 1px solid rgba(23, 33, 25, 0.08);
      background: rgba(255, 255, 255, 0.72);
      color: var(--accent);
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    .hero-card-stamp {
      color: var(--muted);
    }

    .hero-card-title {
      margin: 0;
      font-family: "Newsreader", Georgia, serif;
      font-size: clamp(1.9rem, 3vw, 2.8rem);
      font-weight: 700;
      line-height: 1.02;
      letter-spacing: -0.04em;
      text-wrap: balance;
    }

    .hero-card-summary {
      margin: 0;
      color: var(--muted);
      font-size: 0.95rem;
      line-height: 1.72;
    }

    .hero-card-footer {
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: 1rem;
      margin-top: auto;
    }

    .hero-card-caption {
      margin: 0;
      color: var(--muted);
      font-size: 0.76rem;
      line-height: 1.6;
      max-width: 18rem;
    }

    .hero-card-arrow {
      width: 40px;
      height: 40px;
      flex-shrink: 0;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 999px;
      border: 1px solid rgba(23, 33, 25, 0.10);
      background: rgba(255, 255, 255, 0.84);
      color: var(--accent);
      box-shadow: 0 10px 24px rgba(23, 33, 25, 0.08);
      animation: heroArrowPulse 2s ease-in-out infinite;
    }

    .hero-card-arrow:hover {
      transform: translateY(2px);
    }

    .hero-card-arrow svg {
      width: 16px;
      height: 16px;
      stroke: currentColor;
      fill: none;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
    }

    .hero-card-list {
      display: flex;
      flex-direction: column;
      gap: 0.72rem;
    }

    .hero-card-list-label {
      margin: 0;
      color: var(--muted);
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }

    .hero-card-badge-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.55rem;
    }

    .hero-card-badge {
      display: inline-flex;
      align-items: center;
      min-height: 34px;
      padding: 0 12px;
      border-radius: 999px;
      border: 1px solid rgba(23, 33, 25, 0.10);
      background: rgba(45, 138, 112, 0.08);
      color: var(--text);
      font-size: 0.74rem;
      font-weight: 700;
      letter-spacing: 0.02em;
    }

    .hero-card-note {
      margin: 0;
      color: var(--muted);
      font-size: 0.84rem;
      line-height: 1.68;
    }

    .hero-card-stat-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 0.85rem;
    }

    .hero-card-stat {
      padding: 0.9rem;
      border-radius: 1rem;
      border: 1px solid rgba(23, 33, 25, 0.08);
      background: rgba(255, 255, 255, 0.76);
    }

    .hero-card-stat-label {
      margin: 0;
      color: var(--muted);
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    .hero-card-stat-value {
      margin: 0.4rem 0 0;
      color: var(--text);
      font-family: "Newsreader", Georgia, serif;
      font-size: 1.35rem;
      font-weight: 700;
      letter-spacing: -0.03em;
    }

    .hero-card-stat-copy {
      margin: 0.35rem 0 0;
      color: var(--muted);
      font-size: 0.76rem;
      line-height: 1.55;
    }

    body[data-theme="dark"] .blank-card.is-live {
      background: #1E1E1E;
      border-color: rgba(102, 179, 151, 0.42);
      box-shadow:
        0 0 0 1px rgba(102, 179, 151, 0.14),
        0 24px 64px rgba(0, 0, 0, 0.44),
        0 0 26px rgba(102, 179, 151, 0.12);
      color: #FFFFFF;
    }

    body[data-theme="dark"] .blank-card.is-live::before {
      background:
        radial-gradient(circle at top right, rgba(102, 179, 151, 0.16), transparent 34%),
        linear-gradient(180deg, rgba(255, 255, 255, 0.04), rgba(255, 255, 255, 0));
    }

    body[data-theme="dark"] .hero-card-kicker,
    body[data-theme="dark"] .hero-card-stamp,
    body[data-theme="dark"] .hero-card-badge,
    body[data-theme="dark"] .hero-card-stat {
      background: rgba(255, 255, 255, 0.04);
      border-color: rgba(255, 255, 255, 0.10);
    }

    body[data-theme="dark"] .hero-card-kicker,
    body[data-theme="dark"] .hero-card-arrow {
      color: #8FD3B8;
    }

    body[data-theme="dark"] .hero-card-stamp,
    body[data-theme="dark"] .hero-card-summary,
    body[data-theme="dark"] .hero-card-caption,
    body[data-theme="dark"] .hero-card-list-label,
    body[data-theme="dark"] .hero-card-note,
    body[data-theme="dark"] .hero-card-stat-label,
    body[data-theme="dark"] .hero-card-stat-copy {
      color: rgba(245, 245, 245, 0.78);
    }

    body[data-theme="dark"] .hero-card-title,
    body[data-theme="dark"] .hero-card-stat-value,
    body[data-theme="dark"] .hero-card-badge {
      color: #FFFFFF;
    }

    body[data-theme="dark"] .hero-card-arrow {
      background: rgba(255, 255, 255, 0.05);
      border-color: rgba(102, 179, 151, 0.36);
      box-shadow: 0 10px 26px rgba(0, 0, 0, 0.32), 0 0 18px rgba(102, 179, 151, 0.14);
    }

    .blank-card-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }

    .blank-pill {
      height: 11px;
      border-radius: 999px;
      background: var(--blank-line);
    }

    .blank-pill.short {
      width: 74px;
    }

    .blank-pill.mid {
      width: 96px;
    }

    .blank-pill.long {
      width: 132px;
    }

    .blank-chip-row {
      display: flex;
      gap: 8px;
      align-items: center;
    }

    .blank-chip {
      width: 32px;
      height: 10px;
      border-radius: 999px;
      background: var(--blank-chip-bg);
    }

    .blank-line {
      height: 12px;
      margin-top: 12px;
      border-radius: 999px;
      background: var(--blank-line);
    }

    .blank-line.xl {
      width: 88%;
      height: 20px;
      margin-top: 20px;
    }

    .blank-line.lg {
      width: 78%;
      height: 16px;
    }

    .blank-line.md {
      width: 70%;
    }

    .blank-line.sm {
      width: 48%;
    }

    .blank-card-frame {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
      margin-top: 22px;
    }

    .blank-card-box {
      min-height: 92px;
      border-radius: 1.15rem;
      border: 1px solid rgba(23, 33, 25, 0.06);
      background: var(--blank-card-box-bg);
    }

    .blank-card-footer {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-top: 22px;
      padding-top: 16px;
      border-top: 1px solid rgba(23, 33, 25, 0.06);
    }

    .blank-card-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--accent-bright);
      box-shadow: 0 0 0 7px rgba(45, 138, 112, 0.12);
      flex-shrink: 0;
    }

    .blank-card-footer .blank-line {
      margin-top: 0;
    }

    .btn,
    .btn-ghost,
    .chat-send {
      min-height: 48px;
      padding: 0 18px;
      border-radius: 999px;
      border: 1px solid transparent;
      font-size: 0.92rem;
      font-weight: 700;
      transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease, background-color 0.2s ease;
    }

    .btn {
      color: #FFFFFF;
      background: var(--accent);
      box-shadow: var(--shadow-sm);
    }

    .btn:hover,
    .chat-send:hover {
      transform: translateY(-2px);
      background: var(--accent-dark);
    }

    .btn-ghost {
      color: var(--muted);
      background: var(--ghost-bg);
      border-color: var(--border);
      backdrop-filter: blur(10px);
    }

    .btn-ghost:hover {
      transform: translateY(-2px);
      color: var(--accent);
      background: var(--ghost-hover-bg);
      border-color: rgba(33, 94, 70, 0.24);
    }

    .desk {
      margin-top: -18px;
      padding: 2rem;
    }

    .desk-grid {
      display: grid;
      grid-template-columns: 270px minmax(0, 1fr);
      gap: 1.5rem;
      align-items: center;
    }

    .desk-label {
      margin: 0;
      color: var(--accent);
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
    }

    .desk-title {
      margin: 8px 0 0;
      font-size: 1.45rem;
      font-weight: 800;
      letter-spacing: -0.03em;
    }

    .desk-copy {
      margin: 8px 0 0;
      color: var(--muted);
      font-size: 0.88rem;
      line-height: 1.72;
    }

    .control-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr)) auto auto;
      gap: 12px;
      align-items: center;
    }

    .control,
    .chat-input {
      width: 100%;
      min-height: 48px;
      padding: 0 16px;
      border-radius: 1rem;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--text);
      outline: none;
      box-shadow: var(--shadow-sm);
    }

    .control::placeholder,
    .chat-input::placeholder {
      color: var(--muted-soft);
    }

    .control:focus,
    .chat-input:focus {
      border-color: rgba(33, 94, 70, 0.42);
      box-shadow: 0 0 0 4px rgba(33, 94, 70, 0.08);
    }

    .status-line {
      min-height: 18px;
      margin-top: 12px;
      color: var(--muted);
      font-size: 0.78rem;
      text-align: right;
    }

    .status-line.is-error {
      color: var(--warm-status);
    }

    .stats {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 14px;
      margin-top: 20px;
    }

    .stat {
      padding: 2rem;
    }

    .stat-head {
      display: flex;
      align-items: center;
      gap: 10px;
      color: var(--muted);
      font-size: 0.74rem;
      font-weight: 600;
    }

    .stat-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--accent-soft);
      border: 2px solid var(--accent);
      flex-shrink: 0;
    }

    .stat-value {
      margin-top: 14px;
      font-size: 1.6rem;
      font-weight: 800;
      letter-spacing: -0.04em;
    }

    .stat-copy {
      margin-top: 4px;
      color: var(--muted);
      font-size: 0.78rem;
    }

    .ticker {
      display: flex;
      align-items: center;
      gap: 14px;
      min-height: 48px;
      margin-top: 20px;
      padding: 0 18px;
      overflow: hidden;
      border-radius: 999px;
    }

    .ticker-badge {
      flex-shrink: 0;
      display: inline-flex;
      align-items: center;
      min-height: 30px;
      padding: 0 12px;
      border-radius: 999px;
      background: var(--ticker-badge-bg);
      color: var(--ticker-badge-text);
      font-size: 0.66rem;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    .ticker-window {
      min-width: 0;
      overflow: hidden;
      white-space: nowrap;
      color: var(--muted);
      font-size: 0.84rem;
    }

    .ticker-track {
      display: inline-flex;
      align-items: center;
      gap: 28px;
      animation: tickerMove 92s linear infinite;
    }

    .ticker:hover .ticker-track {
      animation-play-state: paused;
    }

    .ticker-item {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
    }

    .ticker-item strong {
      color: var(--text);
      font-weight: 700;
    }

    .brief {
      display: none;
      margin-top: 20px;
      padding: 2.5rem;
    }

    .brief.is-visible {
      display: block;
    }

    .brief-top {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 12px;
    }

    .brief-label {
      color: var(--accent);
      font-size: 0.68rem;
      font-weight: 800;
      letter-spacing: 0.16em;
      text-transform: uppercase;
    }

    .brief-rule {
      flex: 1;
      height: 1px;
      background: var(--border);
    }

    .brief-text {
      margin: 0;
      font-size: 0.96rem;
      line-height: 1.8;
      color: var(--text);
    }

    .brief-topics {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 14px;
    }

    .brief-topic,
    .meta-pill,
    .trending-pill,
    .lead-fact {
      display: inline-flex;
      align-items: center;
      min-height: 32px;
      padding: 0 12px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: var(--surface-soft);
      color: var(--muted);
      font-size: 0.75rem;
      font-weight: 600;
    }

    .lead-fact {
      background: rgba(255, 253, 249, 0.92);
      color: var(--text);
      font-weight: 700;
    }

    body[data-theme="dark"] .surface,
    body[data-theme="dark"] .insight-card,
    body[data-theme="dark"] .loading-lead,
    body[data-theme="dark"] .quiet-panel {
      background: #1E1E1E;
    }

    body[data-theme="dark"] .insight-card,
    body[data-theme="dark"] .quiet-panel,
    body[data-theme="dark"] .loading-lead {
      border-color: rgba(255, 255, 255, 0.08);
    }

    body[data-theme="dark"] .insight-card--wordcloud .visual-frame,
    body[data-theme="dark"] .wordcloud-frame,
    body[data-theme="dark"] .wordcloud-stage {
      background: transparent;
    }

    body[data-theme="dark"] .lead-headline,
    body[data-theme="dark"] .lead-headline a,
    body[data-theme="dark"] .rail-headline,
    body[data-theme="dark"] .rail-headline a,
    body[data-theme="dark"] .coverage-headline,
    body[data-theme="dark"] .coverage-headline a,
    body[data-theme="dark"] .section-title,
    body[data-theme="dark"] .desk-title,
    body[data-theme="dark"] .quiet-title,
    body[data-theme="dark"] .quiet-title-small {
      color: #FFFFFF;
    }

    body[data-theme="dark"] .lead-summary,
    body[data-theme="dark"] .rail-summary,
    body[data-theme="dark"] .coverage-summary,
    body[data-theme="dark"] .coverage-meta,
    body[data-theme="dark"] .rail-meta,
    body[data-theme="dark"] .lead-note,
    body[data-theme="dark"] .quiet-copy,
    body[data-theme="dark"] .stat-copy,
    body[data-theme="dark"] .desk-copy {
      color: #B0B0B0;
    }

    body[data-theme="dark"] .brief-topic,
    body[data-theme="dark"] .meta-pill,
    body[data-theme="dark"] .trending-pill,
    body[data-theme="dark"] .lead-fact,
    body[data-theme="dark"] .sentiment {
      background: rgba(255, 255, 255, 0.10);
      color: #FFFFFF;
      border-color: rgba(255, 255, 255, 0.12);
    }

    body[data-theme="dark"] .sentiment.positive,
    body[data-theme="dark"] .sentiment.negative,
    body[data-theme="dark"] .sentiment.neutral {
      color: #FFFFFF;
    }

    body[data-theme="dark"] .rail-item:hover {
      background: #232323;
    }

    .section {
      margin-top: 20px;
    }

    .main-grid {
      display: grid;
      grid-template-columns: repeat(12, minmax(0, 1fr));
      gap: 20px;
      align-items: start;
    }

    .lead-card {
      grid-column: span 8;
      padding: 2.5rem;
    }

    .side-column {
      grid-column: span 4;
      display: grid;
      gap: 1rem;
    }

    .news-card,
    .story-card,
    .insight-card,
    .log-card {
      animation: cardRise 0.55s cubic-bezier(0.2, 0.8, 0.2, 1) both;
    }

    .lead-story-layout {
      display: block;
    }

    .lead-story-copy {
      min-width: 0;
    }

    .lead-kicker {
      display: flex;
      align-items: center;
      justify-content: flex-start;
      gap: 12px;
      flex-wrap: wrap;
      padding-bottom: 16px;
      border-bottom: 1px solid rgba(23, 33, 25, 0.08);
    }

    .lead-kicker-left,
    .lead-kicker-right {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: flex-start;
    }

    .lead-body {
      text-align: left;
    }

    .lead-overline {
      margin: 20px 0 0;
      display: flex;
      align-items: center;
      justify-content: flex-start;
      gap: 10px;
      color: var(--accent);
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }

    .lead-headline {
      margin: 18px 0 0;
      max-width: 18ch;
      font-family: "Newsreader", Georgia, serif;
      font-size: clamp(2.5rem, 4.4vw, 3.35rem);
      font-weight: 700;
      line-height: 1.2;
      letter-spacing: -0.02em;
    }

    .lead-headline a:hover,
    .rail-headline a:hover,
    .coverage-headline a:hover,
    .chat-article-title a:hover {
      color: var(--accent);
    }

    .lead-summary {
      margin: 18px 0 0;
      color: var(--muted);
      font-size: 1rem;
      line-height: 1.82;
      max-width: 66ch;
    }

    .lead-facts {
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-start;
      gap: 10px;
      margin-top: 20px;
    }

    .lead-note {
      max-width: 62ch;
      margin: 20px 0 0;
      padding-top: 18px;
      border-top: 1px solid var(--border);
      color: var(--muted);
      font-size: 0.86rem;
      line-height: 1.75;
    }

    .sentiment {
      display: inline-flex;
      align-items: center;
      min-height: 24px;
      padding: 0 10px;
      border-radius: 999px;
      border: 1px solid transparent;
      font-size: 0.68rem;
      font-weight: 700;
    }

    .sentiment.positive {
      background: var(--positive-bg);
      color: var(--positive-text);
      border-color: var(--positive-border);
    }

    .sentiment.negative {
      background: var(--negative-bg);
      color: var(--negative-text);
      border-color: var(--negative-border);
    }

    .sentiment.neutral {
      background: var(--neutral-bg);
      color: var(--neutral-text);
      border-color: var(--neutral-border);
    }

    .rail {
      padding: 2.5rem;
    }

    .rail-item {
      display: block;
      padding: 1.05rem 0;
      border-bottom: 1px solid var(--border);
      transition: transform 0.22s ease, background-color 0.22s ease, box-shadow 0.22s ease;
      border-radius: 1rem;
    }

    .rail-item:last-child {
      border-bottom: 0;
    }

    .rail-item:hover {
      transform: translateY(-4px);
      background: color-mix(in srgb, var(--surface) 75%, var(--surface-soft) 25%);
      box-shadow: var(--shadow-sm);
    }

    .rail-topline {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      flex-wrap: wrap;
    }

    .signal-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--accent);
      box-shadow: 0 0 0 6px rgba(33, 94, 70, 0.14);
      animation: pulse 2.2s ease-in-out infinite;
    }

    .rail-meta {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      color: var(--muted);
      font-size: 0.78rem;
    }

    .rail-source,
    .coverage-source {
      color: var(--text);
      font-weight: 700;
    }

    .rail-body {
      min-width: 0;
      display: grid;
      gap: 8px;
    }

    .meta-dot {
      display: inline-block;
      width: 4px;
      height: 4px;
      border-radius: 50%;
      background: var(--border);
      flex-shrink: 0;
    }

    .rail-headline {
      margin: 0;
      font-size: 1.04rem;
      font-weight: 700;
      line-height: 1.45;
      letter-spacing: -0.02em;
    }

    .rail-summary {
      color: var(--muted);
      font-size: 0.84rem;
      line-height: 1.68;
    }

    .trending {
      display: none;
      padding: 2.5rem;
    }

    .trending.is-visible {
      display: block;
    }

    .trending-list {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .coverage {
      padding: 2.5rem;
    }

    .section-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
      margin-bottom: 18px;
      flex-wrap: wrap;
    }

    .section-title {
      margin: 0;
      font-size: 1.3rem;
      font-weight: 800;
      letter-spacing: -0.04em;
    }

    .count-badge {
      display: none !important;
      align-items: center;
      min-height: 34px;
      padding: 0 12px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: var(--surface-soft);
      color: var(--muted);
      font-size: 0.76rem;
      font-weight: 700;
    }

    .count-badge.is-visible {
      display: inline-flex;
    }

    .coverage-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 16px;
    }

    .coverage-card {
      padding: 2.5rem;
      min-height: 250px;
    }

    .coverage-meta {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      color: var(--muted);
      font-size: 0.78rem;
    }

    .coverage-headline {
      margin: 14px 0 0;
      font-family: "Newsreader", Georgia, serif;
      font-size: 1.22rem;
      font-weight: 700;
      line-height: 1.35;
      letter-spacing: -0.02em;
    }

    .coverage-summary {
      margin-top: 10px;
      color: var(--muted);
      font-size: 0.86rem;
      line-height: 1.72;
    }

    .coverage-link {
      display: inline-flex;
      align-items: center;
      margin-top: 12px;
      color: var(--accent);
      font-size: 0.82rem;
      font-weight: 700;
    }

    .insights {
      padding: 2.5rem;
    }

    #results-container {
      display: none;
    }

    .insights-grid {
      display: grid;
      grid-template-columns: repeat(12, minmax(0, 1fr));
      grid-auto-rows: minmax(200px, auto);
      gap: 1rem;
    }

    .insight-card {
      padding: 1.5rem;
      min-height: 450px;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      overflow: hidden;
      border-radius: 2rem;
      border: 1px solid var(--border);
      background: var(--card-bg);
      background-image: none;
      box-shadow: 0 18px 42px rgba(23, 33, 25, 0.06);
    }

    .insight-card--wordcloud {
      grid-column: span 7;
      grid-row: span 2;
    }

    .insight-card--pie,
    .insight-card--bar {
      grid-column: span 5;
    }

    .insight-card--pie {
      min-height: 500px;
    }

    .insight-card--scatter {
      grid-column: span 12;
      background: var(--card-bg) !important;
    }

    .insight-head {
      margin-bottom: 0;
      flex-shrink: 0;
    }

    .insight-label {
      display: flex;
      align-items: center;
      gap: 8px;
      margin: 0;
      color: var(--muted);
      font-size: 0.66rem;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }

    .insight-label::before {
      content: "";
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--accent);
      flex-shrink: 0;
    }

    .visual-frame {
      flex: 1 1 auto;
      display: flex;
      flex-direction: column;
      width: 100%;
      height: 100%;
      min-height: 390px;
      position: relative;
      padding: 0;
      border-radius: 1.5rem;
      background-color: transparent;
      background-image: none;
      border: 0;
      overflow: hidden;
      box-shadow: none;
    }

    .insight-card--wordcloud .visual-frame {
      min-height: 0;
      background: transparent !important;
    }

    .insight-card--pie .visual-frame {
      min-height: 440px;
      overflow: visible;
    }

    .insight-card--bar .visual-frame {
      animation: barGlow 3.6s ease-in-out infinite;
      box-shadow: 0 0 0 0 rgba(45, 138, 112, 0.12);
    }

    .insight-card--scatter .visual-frame {
      background: transparent !important;
      border-color: transparent !important;
      box-shadow: none !important;
      padding: 0;
      border-radius: 0 !important;
    }

    body[data-theme="dark"] .visual-frame,
    body[data-theme="dark"] .scatter-frame {
      background: transparent !important;
      background-image: none !important;
      border-color: transparent !important;
    }

    .scatter-frame {
      flex: 1 1 auto;
      min-height: 450px;
      height: 100%;
      width: 100%;
      position: relative;
      overflow: hidden;
      border: 0 !important;
      border-radius: 0;
      background: transparent !important;
      background-image: none !important;
      box-shadow: none !important;
      padding: 0;
    }

    .insight-card--scatter #scatter-chart,
    .insight-card--scatter #scatter-chart.visual-frame,
    .insight-card--scatter .visual-frame#scatter-chart {
      background: transparent !important;
      background-image: none !important;
      border: 0 !important;
      border-radius: 0 !important;
      box-shadow: none !important;
      padding: 0 !important;
    }

    #pie-chart,
    #bar-chart,
    #scatter-chart {
      min-height: 390px;
      width: 100%;
      position: relative;
      overflow: hidden;
    }

    #scatter-chart,
    #scatter-chart .js-plotly-plot,
    #scatter-chart .plot-container,
    #scatter-chart .svg-container,
    #scatter-chart .main-svg,
    #scatter-chart .bg {
      background: transparent !important;
      background-image: none !important;
      box-shadow: none !important;
      border: 0 !important;
    }

    #scatter-chart {
      min-height: 450px;
      height: 450px;
    }

    #scatter-chart .bg,
    #scatter-chart .plotbg,
    #scatter-chart .bglayer rect,
    #scatter-chart .cartesianlayer .subplot rect.bg {
      fill: transparent !important;
      stroke: transparent !important;
    }

    #pie-chart {
      min-height: 440px;
      overflow: visible;
    }

    .wordcloud-frame {
      flex: 1 1 auto;
      min-height: 0;
      display: flex;
      align-items: stretch;
      background: transparent !important;
    }

    .wordcloud-stage {
      flex: 1 1 auto;
      width: 100%;
      min-height: 100%;
      height: 100%;
      border-radius: 1.25rem;
      border: 0;
      background-color: transparent !important;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      padding: 0;
    }

    .wordcloud-image {
      display: block;
      width: 100%;
      height: 100%;
      max-height: 100%;
      object-fit: contain;
      margin: 0 auto;
    }

    .wordcloud-stage.is-loading {
      position: relative;
      overflow: hidden;
      background:
        linear-gradient(135deg, rgba(33, 94, 70, 0.05), rgba(98, 111, 125, 0.08)),
        var(--surface-soft);
    }

    .wordcloud-stage.is-loading::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.86), transparent);
      transform: translateX(-100%);
      animation: shimmer 1.25s linear infinite;
    }

    .visual-empty {
      width: 100%;
      min-height: 100%;
      height: 100%;
      border-radius: 1.25rem;
      background: transparent;
    }

    .agent-log {
      display: none;
      margin-top: 22px;
    }

    .agent-log.is-visible {
      display: block;
    }

    .log-toggle {
      width: 100%;
      min-height: 56px;
      padding: 0 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      border-radius: 1.25rem;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--muted);
      font-size: 0.88rem;
      font-weight: 700;
      text-align: left;
      box-shadow: var(--shadow-sm);
    }

    .log-chevron {
      color: var(--accent);
      transition: transform 0.2s ease;
    }

    .agent-log.is-open .log-chevron {
      transform: rotate(180deg);
    }

    .log-content {
      display: none;
      margin-top: 14px;
      gap: 14px;
    }

    .agent-log.is-open .log-content {
      display: grid;
    }

    .log-card {
      padding: 2.5rem;
    }

    .log-topic {
      margin: 0 0 12px;
      font-size: 1rem;
      font-weight: 800;
      letter-spacing: -0.02em;
    }

    .log-entry + .log-entry {
      margin-top: 12px;
      padding-top: 12px;
      border-top: 1px solid var(--border);
    }

    .log-stage {
      display: block;
      margin-bottom: 5px;
      color: var(--accent);
      font-size: 0.62rem;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    .log-message {
      color: var(--text);
      font-size: 0.84rem;
      line-height: 1.72;
    }

    .quiet-card {
      padding: 2.5rem;
    }

    .quiet-panel {
      border-radius: 1.5rem;
      border: 1px solid var(--border);
      background:
        radial-gradient(circle at top left, rgba(33, 94, 70, 0.10), transparent 28%),
        linear-gradient(180deg, #FFFFFF 0%, #F7F7F5 100%);
      padding: 2rem;
      min-height: 320px;
      display: flex;
      align-items: flex-end;
    }

    .quiet-kicker {
      display: inline-flex;
      align-items: center;
      min-height: 30px;
      padding: 0 11px;
      border-radius: 999px;
      background: #FFFFFF;
      border: 1px solid var(--border);
      color: var(--accent);
      font-size: 0.7rem;
      font-weight: 800;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    .quiet-title {
      margin: 12px 0 0;
      font-family: "Newsreader", Georgia, serif;
      font-size: 1.42rem;
      font-weight: 700;
      line-height: 1.28;
      letter-spacing: -0.03em;
    }

    .quiet-copy {
      margin: 8px 0 0;
      color: var(--muted);
      font-size: 0.88rem;
      line-height: 1.72;
    }

    .quiet-rail {
      display: grid;
      gap: 12px;
      padding: 2rem;
    }

    .quiet-rail-row {
      padding: 16px 0;
      border-bottom: 1px solid var(--border);
    }

    .quiet-rail-row:last-child {
      border-bottom: 0;
    }

    .quiet-label {
      color: var(--accent);
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    .quiet-title-small {
      margin-top: 5px;
      font-size: 0.94rem;
      font-weight: 700;
      line-height: 1.5;
    }

    .quiet-muted {
      margin-top: 6px;
      color: var(--muted);
      font-size: 0.82rem;
      line-height: 1.65;
    }

    .skeleton-box,
    .skeleton-line,
    .skeleton-pill {
      position: relative;
      overflow: hidden;
      background: #E2E8E1;
    }

    .skeleton-box::after,
    .skeleton-line::after,
    .skeleton-pill::after {
      content: "";
      position: absolute;
      inset: 0;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.74), transparent);
      transform: translateX(-100%);
      animation: shimmer 1.2s linear infinite;
    }

    .loading-lead {
      padding: 2.5rem;
      border-radius: 1.5rem;
      border: 1px solid var(--border);
      background: rgba(255, 255, 255, 0.88);
    }

    .loading-lead-copy {
      min-width: 0;
    }

    .skeleton-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 16px;
      justify-content: flex-start;
    }

    .skeleton-pill {
      height: 28px;
      border-radius: 999px;
    }

    .skeleton-pill.wide {
      width: 112px;
    }

    .skeleton-pill.mid {
      width: 80px;
    }

    .skeleton-line {
      height: 12px;
      margin-top: 10px;
      border-radius: 999px;
    }

    .skeleton-line.lg {
      width: 90%;
      height: 20px;
    }

    .skeleton-line.xl {
      width: 92%;
      height: 26px;
    }

    .skeleton-line.md {
      width: 76%;
    }

    .skeleton-line.sm {
      width: 52%;
    }

    .loading-rail {
      padding: 2.5rem;
    }

    .loading-rail-row {
      padding: 18px 0;
      border-bottom: 1px solid var(--border);
    }

    .loading-rail-row:last-child {
      border-bottom: 0;
    }

    .loading-coverage {
      padding: 2.5rem;
      min-height: 220px;
    }

    .chat-launch {
      position: fixed;
      right: 22px;
      bottom: 22px;
      z-index: 9999;
      display: inline-flex;
      align-items: center;
      gap: 12px;
      min-height: 58px;
      padding: 0 16px 0 14px;
      border: 1px solid rgba(23, 33, 25, 0.08);
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.94);
      color: var(--text);
      box-shadow: 0 18px 38px rgba(23, 33, 25, 0.12);
    }

    .chat-launch-mark {
      width: 30px;
      height: 30px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 10px;
      background: rgba(45, 138, 112, 0.10);
      color: var(--accent);
      flex-shrink: 0;
    }

    .chat-launch-mark svg,
    .chat-bot-mark svg {
      width: 16px;
      height: 16px;
      stroke: currentColor;
      fill: none;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
    }

    .chat-launch-copy {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      line-height: 1.1;
    }

    .chat-launch-label {
      color: var(--muted);
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    .chat-launch-title {
      margin-top: 4px;
      color: var(--text);
      font-size: 0.92rem;
      font-weight: 700;
    }

    .chat-launch-status {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--accent-bright);
      box-shadow: 0 0 0 5px rgba(45, 138, 112, 0.16);
      flex-shrink: 0;
      animation: pulse 3s ease-in-out infinite;
    }

    .chat-overlay {
      position: fixed;
      inset: 0;
      background: rgba(26, 26, 26, 0.16);
      opacity: 0;
      pointer-events: none;
      z-index: 9997;
      transition: opacity 0.22s ease;
    }

    .chat-overlay.is-visible {
      opacity: 1;
      pointer-events: auto;
    }

    .chat-panel {
      position: fixed;
      right: 22px;
      bottom: 92px;
      width: 390px;
      max-width: calc(100vw - 28px);
      height: min(720px, calc(100vh - 120px));
      display: flex;
      flex-direction: column;
      overflow: hidden;
      border-radius: 1.75rem;
      border: 1px solid rgba(229, 231, 235, 0.95);
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(18px);
      box-shadow: var(--shadow-lg);
      transform: translateY(18px) scale(0.98);
      opacity: 0;
      pointer-events: none;
      z-index: 9998;
      transition: transform 0.22s ease, opacity 0.22s ease;
    }

    .chat-panel.is-open {
      transform: translateY(0) scale(1);
      opacity: 1;
      pointer-events: auto;
    }

    .chat-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding: 18px;
      border-bottom: 1px solid rgba(229, 231, 235, 0.9);
      background: linear-gradient(180deg, rgba(255, 255, 255, 0.98), rgba(248, 247, 244, 0.92));
    }

    .chat-brand {
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 0;
    }

    .chat-bot-mark {
      width: 40px;
      height: 40px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      border-radius: 14px;
      background: linear-gradient(145deg, #1A563F 0%, #2C7B5D 100%);
      color: #FFFFFF;
      flex-shrink: 0;
    }

    .chat-brand-title {
      font-size: 0.96rem;
      font-weight: 800;
    }

    .chat-brand-sub {
      margin-top: 3px;
      color: var(--muted);
      font-size: 0.76rem;
    }

    .chat-close {
      width: 38px;
      height: 38px;
      border: 1px solid var(--border);
      border-radius: 12px;
      background: var(--surface);
      color: var(--muted);
      font-size: 1rem;
      font-weight: 700;
      box-shadow: var(--shadow-sm);
    }

    .chat-close:hover {
      background: #FFFFFF;
      color: var(--text);
    }

    .chat-subhead {
      padding: 10px 18px 12px;
      color: var(--muted);
      font-size: 0.76rem;
      border-bottom: 1px solid rgba(229, 231, 235, 0.7);
      background: rgba(255, 255, 255, 0.84);
    }

    .chat-messages {
      flex: 1;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
      padding: 16px 18px;
      scrollbar-width: thin;
      scrollbar-color: rgba(26, 26, 26, 0.18) transparent;
    }

    .chat-bubble {
      max-width: 100%;
      font-size: 0.86rem;
      line-height: 1.65;
    }

    .chat-bubble.user {
      align-self: flex-end;
      max-width: 84%;
      padding: 12px 14px;
      border-radius: 20px 20px 8px 20px;
      background: #1A1A1A;
      color: #FFFFFF;
      box-shadow: var(--shadow-sm);
    }

    .chat-bubble.bot {
      align-self: flex-start;
      width: 100%;
      padding: 12px 14px;
      border-radius: 20px 20px 20px 8px;
      background: var(--surface-soft);
      border: 1px solid var(--border);
      color: var(--text);
    }

    .chat-bubble p {
      margin: 0;
    }

    .chat-articles {
      display: grid;
      gap: 8px;
      margin-top: 10px;
    }

    .chat-article {
      padding: 10px 12px;
      border-radius: 1rem;
      border: 1px solid var(--border);
      border-left: 3px solid var(--accent);
      background: #FFFFFF;
    }

    .chat-article.positive {
      border-left-color: var(--positive-text);
    }

    .chat-article.negative {
      border-left-color: var(--negative-text);
    }

    .chat-article-title {
      margin: 0;
      font-size: 0.84rem;
      font-weight: 700;
      line-height: 1.45;
    }

    .chat-article-meta,
    .chat-commentary {
      margin-top: 4px;
      color: var(--muted);
      font-size: 0.74rem;
      line-height: 1.55;
    }

    .chat-suggestions {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      padding: 10px 18px 0;
    }

    .chat-chip,
    .quick-briefing {
      min-height: 34px;
      padding: 0 12px;
      border-radius: 999px;
      border: 1px solid var(--border);
      background: var(--surface-soft);
      color: var(--muted);
      font-size: 0.76rem;
      font-weight: 600;
      transition: transform 0.2s ease, border-color 0.2s ease, color 0.2s ease, background-color 0.2s ease;
    }

    .chat-chip:hover,
    .quick-briefing:hover {
      transform: translateY(-1px);
      border-color: rgba(33, 94, 70, 0.24);
      color: var(--accent);
      background: #FFFFFF;
    }

    .quick-briefing {
      margin: 12px 18px 0;
      border-color: rgba(45, 138, 112, 0.28);
      background: #2D8A70;
      color: #FFFFFF;
      box-shadow: 0 12px 26px rgba(45, 138, 112, 0.18);
    }

    .chat-input-row {
      display: flex;
      gap: 10px;
      padding: 16px 18px 18px;
      border-top: 1px solid rgba(229, 231, 235, 0.75);
      background: linear-gradient(180deg, rgba(255, 255, 255, 0.78), rgba(255, 255, 255, 0.96));
    }

    .chat-send {
      min-width: 84px;
      color: #FFFFFF;
      background: #2D8A70;
    }

    .quick-briefing:hover,
    .chat-send:hover {
      background: #246F5A;
      color: #FFFFFF;
    }

    body[data-theme="dark"] .chat-launch {
      border: 1px solid rgba(255, 255, 255, 0.10);
      background: #1E1E1E;
      color: #F5F5F5;
      box-shadow: 0 18px 38px rgba(0, 0, 0, 0.40);
    }

    body[data-theme="dark"] .chat-launch-label {
      color: #B0B0B0;
    }

    body[data-theme="dark"] .chat-launch-title {
      color: #FFFFFF;
    }

    body[data-theme="dark"] .chat-launch-mark {
      background: rgba(45, 138, 112, 0.18);
      color: #DDF7EE;
    }

    body[data-theme="dark"] .chat-launch-status {
      background: #2D8A70;
      box-shadow: 0 0 0 5px rgba(45, 138, 112, 0.20);
    }

    body[data-theme="dark"] .chat-overlay {
      background: rgba(0, 0, 0, 0.46);
    }

    body[data-theme="dark"] .chat-panel {
      border: 1px solid rgba(255, 255, 255, 0.10);
      background: #1E1E1E;
      backdrop-filter: none;
      box-shadow: 0 32px 80px rgba(0, 0, 0, 0.48);
    }

    body[data-theme="dark"] .chat-header {
      border-bottom: 1px solid rgba(255, 255, 255, 0.10);
      background: #1E1E1E;
    }

    body[data-theme="dark"] .chat-brand-title,
    body[data-theme="dark"] .chat-bubble.bot,
    body[data-theme="dark"] .chat-bubble.bot p,
    body[data-theme="dark"] .chat-bubble.user,
    body[data-theme="dark"] .chat-article-title,
    body[data-theme="dark"] .chat-article-title a {
      color: #FFFFFF;
    }

    body[data-theme="dark"] .chat-brand-sub,
    body[data-theme="dark"] .chat-subhead,
    body[data-theme="dark"] .chat-article-meta,
    body[data-theme="dark"] .chat-commentary {
      color: #B0B0B0;
    }

    body[data-theme="dark"] .chat-close {
      border: 1px solid rgba(255, 255, 255, 0.12);
      background: #121212;
      color: #F5F5F5;
      box-shadow: none;
    }

    body[data-theme="dark"] .chat-close:hover {
      background: #181818;
      color: #FFFFFF;
    }

    body[data-theme="dark"] .chat-subhead {
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      background: #1E1E1E;
    }

    body[data-theme="dark"] .chat-messages {
      background: #1E1E1E;
      scrollbar-color: rgba(255, 255, 255, 0.16) transparent;
    }

    body[data-theme="dark"] .chat-bubble.user {
      background: #2D8A70;
      box-shadow: none;
    }

    body[data-theme="dark"] .chat-bubble.bot {
      background: #232323;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    body[data-theme="dark"] .chat-article {
      background: #121212;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    body[data-theme="dark"] .chat-input-row {
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      background: #1E1E1E;
    }

    body[data-theme="dark"] .chat-input {
      background: #121212;
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: #FFFFFF;
      box-shadow: none;
    }

    body[data-theme="dark"] .chat-input::placeholder {
      color: #8F8F8F;
    }

    body[data-theme="dark"] .chat-input:focus {
      border-color: rgba(45, 138, 112, 0.56);
      box-shadow: 0 0 0 4px rgba(45, 138, 112, 0.12);
    }

    body[data-theme="dark"] .quick-briefing,
    body[data-theme="dark"] .chat-send {
      border-color: transparent;
      background: #2D8A70;
      color: #FFFFFF;
      box-shadow: none;
    }

    body[data-theme="dark"] .quick-briefing:hover,
    body[data-theme="dark"] .chat-send:hover {
      background: #246F5A;
      color: #FFFFFF;
    }

    .is-loading {
      opacity: 0.65;
      pointer-events: none;
    }

    .visually-hidden {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    }

    @keyframes tickerMove {
      from { transform: translateX(0); }
      to { transform: translateX(-50%); }
    }

    @keyframes synthesisPulse {
      0% { transform: translateX(-120%); }
      55% { transform: translateX(100%); }
      100% { transform: translateX(220%); }
    }

    @keyframes shimmer {
      from { transform: translateX(-100%); }
      to { transform: translateX(100%); }
    }

    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(0.9); opacity: 0.58; }
    }

    @keyframes trackingInExpand {
      0% {
        opacity: 0;
        letter-spacing: 0.08em;
        transform: translateY(10px);
      }
      100% {
        opacity: 1;
        letter-spacing: 0.28em;
        transform: translateY(0);
      }
    }

    @keyframes barGlow {
      0%, 100% {
        box-shadow: 0 0 0 0 rgba(45, 138, 112, 0.10);
      }
      50% {
        box-shadow: 0 18px 34px rgba(45, 138, 112, 0.16);
      }
    }

    @keyframes heroArrowPulse {
      0%, 100% {
        transform: translateY(0);
        box-shadow: 0 10px 24px rgba(23, 33, 25, 0.08);
      }
      50% {
        transform: translateY(6px);
        box-shadow: 0 16px 30px rgba(23, 33, 25, 0.12);
      }
    }

    @keyframes cardRise {
      from {
        opacity: 0;
        transform: translateY(16px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @media (max-width: 1220px) {
      .desk-grid,
      .stats,
      .coverage-grid {
        grid-template-columns: 1fr 1fr;
      }

      .main-grid {
        grid-template-columns: 1fr;
      }

      .lead-card,
      .side-column {
        grid-column: span 1;
      }

      .control-grid {
        grid-template-columns: repeat(3, minmax(0, 1fr));
      }

      .control-grid #fetchBtn,
      .control-grid #sampleBtn {
        grid-column: span 1;
      }

      .blank-stack {
        width: min(720px, 100%);
      }
    }

    @media (max-width: 900px) {
      .shell {
        padding-left: 18px;
        padding-right: 18px;
      }

      .hero {
        padding-left: 18px;
        padding-right: 18px;
      }

      .desk-grid,
      .stats,
      .coverage-grid {
        grid-template-columns: 1fr;
      }

      .control-grid {
        grid-template-columns: 1fr 1fr;
      }

      .hero-actions .control {
        min-width: 190px;
      }

      .status-line {
        text-align: left;
      }

      .blank-stack {
        width: min(620px, 100%);
        height: 380px;
      }

      .blank-card {
        width: min(340px, calc(100% - 20px));
      }

      .hero-card-title {
        font-size: clamp(1.7rem, 4.2vw, 2.35rem);
      }

      .hero-card-stat-grid {
        grid-template-columns: 1fr;
      }

      .blank-card--one {
        --card-transform: translateX(calc(-50% + 38px)) rotate(6deg) translateY(28px);
        --card-transform-hidden: translateX(calc(-50% + 38px)) rotate(6deg) translateY(54px) scale(0.985);
        --card-transform-loaded: translateX(calc(-50% + 52px)) rotate(7deg) translateY(22px);
        --card-transform-hover: translateX(calc(-50% + 320px)) rotate(2deg) translateY(4px);
        left: 50%;
        bottom: 28px;
      }

      .blank-card--two {
        --card-transform: translateX(calc(-50% - 38px)) rotate(-6deg) translateY(28px);
        --card-transform-hidden: translateX(calc(-50% - 38px)) rotate(-6deg) translateY(54px) scale(0.985);
        --card-transform-loaded: translateX(calc(-50% - 52px)) rotate(-7deg) translateY(16px);
        --card-transform-hover: translateX(calc(-50% - 320px)) rotate(-2deg) translateY(4px);
        left: 50%;
        bottom: 28px;
      }

      .blank-card--three {
        --card-transform-loaded: translateX(-50%) translateY(-8px) scale(1);
        --card-transform-hover: translateX(-50%) translateY(-10px) scale(1);
        width: min(430px, calc(100% - 12px));
      }

      .insights-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
      }

      .insight-card--wordcloud,
      .insight-card--scatter {
        grid-column: span 2;
      }

      .insight-card--pie,
      .insight-card--bar {
        grid-column: span 1;
      }
    }

    @media (max-width: 720px) {
      .logo-wrapper {
        font-size: 2.35rem;
      }

      .hero-visuals {
        padding-left: 0;
        padding-right: 0;
        min-height: 340px;
      }

      .hero-actions .control,
      .hero-actions .theme-toggle,
      .hero-actions .btn,
      .hero-actions .btn-ghost {
        width: 100%;
      }

      .blank-stack {
        width: min(100%, 400px);
        height: 300px;
      }

      .blank-card {
        width: min(248px, calc(100% - 10px));
        min-height: 188px;
        padding: 1rem;
        border-radius: 1.25rem;
      }

      .hero-card-shell {
        gap: 0.75rem;
      }

      .hero-card-meta,
      .hero-card-footer {
        align-items: flex-start;
        flex-direction: column;
      }

      .hero-card-title {
        font-size: 1.45rem;
      }

      .hero-card-summary,
      .hero-card-note,
      .hero-card-caption {
        font-size: 0.78rem;
        line-height: 1.58;
      }

      .hero-card-arrow {
        width: 34px;
        height: 34px;
      }

      .blank-card--one {
        --card-transform: translateX(calc(-50% + 28px)) rotate(5deg) translateY(22px);
        --card-transform-hidden: translateX(calc(-50% + 28px)) rotate(5deg) translateY(46px) scale(0.985);
        --card-transform-loaded: translateX(calc(-50% + 38px)) rotate(6deg) translateY(18px);
        --card-transform-hover: translateX(calc(-50% + 320px)) rotate(2deg) translateY(4px);
        left: 50%;
        bottom: 22px;
      }

      .blank-card--two {
        --card-transform: translateX(calc(-50% - 28px)) rotate(-5deg) translateY(22px);
        --card-transform-hidden: translateX(calc(-50% - 28px)) rotate(-5deg) translateY(46px) scale(0.985);
        --card-transform-loaded: translateX(calc(-50% - 38px)) rotate(-6deg) translateY(14px);
        --card-transform-hover: translateX(calc(-50% - 320px)) rotate(-2deg) translateY(4px);
        left: 50%;
        bottom: 22px;
      }

      .blank-card--three {
        --card-transform-loaded: translateX(-50%) translateY(-6px) scale(1);
        --card-transform-hover: translateX(-50%) translateY(-10px) scale(1);
        width: min(300px, calc(100% - 6px));
        min-height: 214px;
      }

      .blank-card-frame {
        grid-template-columns: 1fr;
      }

      .insights-grid {
        grid-template-columns: 1fr;
      }

      .insight-card--wordcloud,
      .insight-card--pie,
      .insight-card--bar,
      .insight-card--scatter {
        grid-column: span 1;
      }

      .control-grid {
        grid-template-columns: 1fr;
      }

      .chat-launch {
        right: 18px;
        bottom: 18px;
      }

      .chat-panel {
        right: 16px;
        bottom: 86px;
        width: calc(100vw - 32px);
        height: min(720px, calc(100vh - 118px));
      }
    }
  </style>
</head>
<body>
  <header class="hero">
    <div class="hero-inner">
      <div class="logo-wrapper" role="heading" aria-level="1" aria-label="VeritasAI">
        <span class="veritas-serif">Ver<span class="veritas-i">ı</span>tas</span>
        <span class="ai-sans">AI</span>
      </div>
      <p class="hero-tagline">PRECISION NEWS SYNTHESIS</p>
      <p class="hero-copy">
        VeritasAI transforms fragmented RSS streams into a singular, cohesive news experience.
        By prioritizing signal over noise, it synthesizes global coverage into an actionable live edition with integrated visual analysis.
      </p>
      <div class="hero-actions">
        <select class="control" id="languageSelect" aria-label="Language">
          <option value="English">English (Direct)</option>
          <option value="Spanish">Spanish (Neural Translation)</option>
          <option value="Hindi">Hindi (Neural Translation)</option>
          <option value="French">French (Neural Translation)</option>
          <option value="German">German (Neural Translation)</option>
        </select>
        <button class="btn" id="heroFetchBtn" type="button">Build Live Edition</button>
        <button class="theme-toggle" id="themeToggle" type="button" aria-pressed="false">Dark Mode</button>
        <button class="btn-ghost" id="heroInsightsBtn" type="button">See Insights</button>
      </div>
      <div class="hero-visuals" id="heroVisuals">
        <div class="blank-stack" id="heroBlankStack">
          <article class="blank-card blank-card--one">
            <div class="blank-card-top">
              <span class="blank-pill short"></span>
              <div class="blank-chip-row">
                <span class="blank-chip"></span>
                <span class="blank-chip"></span>
              </div>
            </div>
            <div class="blank-line xl"></div>
            <div class="blank-line lg"></div>
            <div class="blank-line md"></div>
            <div class="blank-card-frame">
              <div class="blank-card-box"></div>
              <div class="blank-card-box"></div>
            </div>
          </article>
          <article class="blank-card blank-card--two">
            <div class="blank-card-top">
              <span class="blank-pill mid"></span>
              <div class="blank-chip-row">
                <span class="blank-chip"></span>
                <span class="blank-chip"></span>
                <span class="blank-chip"></span>
              </div>
            </div>
            <div class="blank-line xl"></div>
            <div class="blank-line lg"></div>
            <div class="blank-line sm"></div>
            <div class="blank-card-footer">
              <span class="blank-card-dot"></span>
              <div class="blank-line md"></div>
            </div>
          </article>
          <article class="blank-card blank-card--three">
            <div class="blank-card-top">
              <span class="blank-pill long"></span>
              <div class="blank-chip-row">
                <span class="blank-chip"></span>
                <span class="blank-chip"></span>
              </div>
            </div>
            <div class="blank-line xl"></div>
            <div class="blank-line lg"></div>
            <div class="blank-line md"></div>
            <div class="blank-line sm"></div>
            <div class="blank-card-frame">
              <div class="blank-card-box"></div>
              <div class="blank-card-box"></div>
            </div>
            <div class="blank-card-footer">
              <span class="blank-card-dot"></span>
              <div class="blank-line lg"></div>
            </div>
          </article>
        </div>
        <div class="synthesis-progress" id="heroSynthesisProgress" hidden>
          <div class="synthesis-progress-shell">
            <p class="synthesis-progress-title">Synthesis Terminal</p>
            <div class="synthesis-progress-track" aria-hidden="true"></div>
            <p class="synthesis-progress-message" id="synthesisProgressMessage" aria-live="polite">
              Initializing Neural Engines...
            </p>
            <button class="synthesis-progress-cancel" id="cancelRequestBtn" type="button">Cancel Synthesis</button>
          </div>
        </div>
      </div>
    </div>
  </header>

  <div class="shell">
    <section class="desk surface interactive" id="desk">
      <div class="desk-grid">
        <div>
          <p class="desk-label">Editorial Desk</p>
          <h2 class="desk-title">Curate the live edition.</h2>
          <p class="desk-copy">Search by topic, switch languages on demand, and move from live coverage to reasoning and visuals without leaving the desk.</p>
        </div>
        <div>
          <div class="control-grid">
            <input class="control" id="topic1" type="text" placeholder="Topic 1" aria-label="Topic 1" />
            <input class="control" id="topic2" type="text" placeholder="Topic 2" aria-label="Topic 2" />
            <input class="control" id="topic3" type="text" placeholder="Topic 3" aria-label="Topic 3" />
            <button class="btn" id="fetchBtn" type="button">Fetch News</button>
            <button class="btn-ghost" id="sampleBtn" type="button">Load Sample Topics</button>
          </div>
          <div class="status-line" id="statusLine" aria-live="polite"></div>
        </div>
      </div>
    </section>

    <section class="stats" aria-label="Edition metrics">
      <article class="surface interactive stat">
        <div class="stat-head"><span class="stat-dot"></span>Stories surfaced</div>
        <div class="stat-value" id="statArticles">—</div>
        <div class="stat-copy">Article count in the current edition.</div>
      </article>
      <article class="surface interactive stat">
        <div class="stat-head"><span class="stat-dot"></span>Topics active</div>
        <div class="stat-value" id="statTopics">—</div>
        <div class="stat-copy">Prompt count shaping the desk.</div>
      </article>
      <article class="surface interactive stat">
        <div class="stat-head"><span class="stat-dot"></span>Positive share</div>
        <div class="stat-value" id="statPositive">—</div>
        <div class="stat-copy">Positive sentiment within fetched coverage.</div>
      </article>
      <article class="surface interactive stat">
        <div class="stat-head"><span class="stat-dot"></span>Latest timestamp</div>
        <div class="stat-value" id="statLatest">—</div>
        <div class="stat-copy">Most recent story timestamp in the edition.</div>
      </article>
    </section>

    <section class="surface ticker" aria-label="Live ticker">
      <div class="ticker-badge">Live</div>
      <div class="ticker-window">
        <div class="ticker-track" id="tickerTrack"></div>
      </div>
    </section>

    <section class="surface brief" id="briefCard" hidden>
      <div class="brief-top">
        <div class="brief-label">Briefing</div>
        <div class="brief-rule"></div>
      </div>
      <p class="brief-text" id="briefText"></p>
      <div class="brief-topics" id="briefTopics"></div>
    </section>

    <section class="section" id="editionStage">
      <div class="main-grid">
        <article class="surface interactive lead-card" id="heroArticle"></article>
        <div class="side-column">
          <section class="surface rail" id="secondaryArticles"></section>
          <section class="surface trending interactive" id="trendingSection">
            <div class="trending-list" id="trendingSources"></div>
          </section>
        </div>
      </div>
    </section>

    <div id="results-container">
      <section class="section surface coverage">
        <div class="section-head">
          <div><h2 class="section-title">More Coverage</h2></div>
          <div class="count-badge" id="coverageCount"></div>
        </div>
        <div class="coverage-grid" id="coverageGrid"></div>
      </section>

      <section class="section surface insights" id="insightsBand">
        <div class="section-head">
          <div><h2 class="section-title">Insights</h2></div>
        </div>
        <div class="insights-grid">
          <article class="surface insight-card insight-card--wordcloud interactive">
            <div class="insight-head">
              <p class="insight-label">Word Cloud</p>
            </div>
            <div class="visual-frame wordcloud-frame" id="wordcloudFrame">
              <div class="wordcloud-stage is-loading"></div>
            </div>
          </article>
          <article class="surface insight-card insight-card--pie interactive">
            <div class="insight-head">
              <p class="insight-label">Sentiment Pie</p>
            </div>
            <div class="visual-frame" id="pie-chart"></div>
          </article>
          <article class="surface insight-card insight-card--bar interactive">
            <div class="insight-head">
              <p class="insight-label">Keyword Bar</p>
            </div>
            <div class="visual-frame" id="bar-chart"></div>
          </article>
          <article class="surface insight-card insight-card--scatter interactive">
            <div class="insight-head">
              <p class="insight-label">Sentiment Scatter</p>
            </div>
            <div class="scatter-frame" id="scatter-chart"></div>
          </article>
        </div>
      </section>
    </div>

    <section class="agent-log" id="agentLogSection" hidden>
      <button class="log-toggle" id="agentLogToggle" type="button" aria-expanded="false">
        <span>Agent Reasoning Log</span>
        <span class="log-chevron">▾</span>
      </button>
      <div class="log-content" id="agentLogContent"></div>
    </section>
  </div>

  <button class="chat-launch interactive" id="chatFab" type="button" aria-label="Open VeritasBot" aria-expanded="false">
    <span class="chat-launch-mark" aria-hidden="true">
      <svg viewBox="0 0 24 24">
        <path d="M6 7h12"></path>
        <path d="M6 12h10"></path>
        <path d="M6 17h7"></path>
      </svg>
    </span>
    <span class="chat-launch-copy">
      <span class="chat-launch-label">Assistant</span>
      <span class="chat-launch-title">Ask Veritas</span>
    </span>
    <span class="chat-launch-status" aria-hidden="true"></span>
  </button>

  <div class="chat-overlay" id="chatOverlay"></div>

  <aside class="chat-panel" id="chatPanel" aria-hidden="true">
    <div class="chat-header">
      <div class="chat-brand">
        <span class="chat-bot-mark" aria-hidden="true">
          <svg viewBox="0 0 24 24">
            <path d="M6 7h12"></path>
            <path d="M6 12h10"></path>
            <path d="M6 17h7"></path>
          </svg>
        </span>
        <div>
          <div class="chat-brand-title">VeritasBot</div>
          <div class="chat-brand-sub">Ask about the live edition or request a briefing.</div>
        </div>
      </div>
      <button class="chat-close" id="chatCloseBtn" type="button" aria-label="Close chat panel">×</button>
    </div>
    <div class="chat-subhead">The assistant uses the same live article set rendered on the page.</div>
    <div class="chat-messages" id="chatMessages">
      <div class="chat-bubble bot">
        <p>Try a briefing, ask what is trending, or search for a company, market, or event.</p>
      </div>
    </div>
    <div class="chat-suggestions" id="suggestionChips"></div>
    <button class="quick-briefing" id="quickBriefingBtn" type="button">Quick Briefing</button>
    <div class="chat-input-row">
      <label class="visually-hidden" for="chatInput">Chat message</label>
      <input class="chat-input" id="chatInput" type="text" placeholder="Ask VeritasBot about the news" />
      <button class="chat-send" id="chatSendBtn" type="button">Ask</button>
    </div>
  </aside>

  <script>
    let allArticles = [];
    let originalArticles = [];
    let chatHistory = [];
    let lastTopic = null;
    let chatPanelOpen = false;

    let latestBriefing = "";
    let currentTopics = [];
    let reasoningData = {};
    let latestEditionTimestamp = null;
    let translationRequestId = 0;
    let agentLogOpen = false;
    let hasSuccessfulFetch = false;
    let backendWarmupPromise = null;

    const DEFAULT_SUGGESTIONS = [
      "Give me a briefing",
      "Find news on Nvidia",
      "What is trending?"
    ];

    const DEFAULT_TICKER = [
      { topic: "Edition", headline: "A curated front page will appear after the first fetch." },
      { topic: "Coverage", headline: "Lead story, side rail, deeper grid, visuals, and chat stay in sync." },
      { topic: "Assistant", headline: "Ask follow-up questions without leaving the live edition." }
    ];

    const RELIABLE_SOURCES = [
      "Reuters",
      "Associated Press",
      "AP",
      "BBC",
      "Bloomberg",
      "Financial Times",
      "The New York Times",
      "The Wall Street Journal",
      "The Guardian",
      "CNBC"
    ];

    const topicInputs = [
      document.getElementById("topic1"),
      document.getElementById("topic2"),
      document.getElementById("topic3")
    ];

    const heroFetchBtn = document.getElementById("heroFetchBtn");
    const heroInsightsBtn = document.getElementById("heroInsightsBtn");
    const themeToggle = document.getElementById("themeToggle");
    const fetchBtn = document.getElementById("fetchBtn");
    const sampleBtn = document.getElementById("sampleBtn");
    const languageSelect = document.getElementById("languageSelect");
    const statusLine = document.getElementById("statusLine");
    const tickerTrack = document.getElementById("tickerTrack");
    const briefCard = document.getElementById("briefCard");
    const briefText = document.getElementById("briefText");
    const briefTopics = document.getElementById("briefTopics");
    const heroArticle = document.getElementById("heroArticle");
    const secondaryArticles = document.getElementById("secondaryArticles");
    const trendingSection = document.getElementById("trendingSection");
    const trendingSources = document.getElementById("trendingSources");
    const coverageGrid = document.getElementById("coverageGrid");
    const coverageCount = document.getElementById("coverageCount");
    const insightsBand = document.getElementById("insightsBand");
    const resultsContainer = document.getElementById("results-container");
    const agentLogSection = document.getElementById("agentLogSection");
    const agentLogToggle = document.getElementById("agentLogToggle");
    const agentLogContent = document.getElementById("agentLogContent");
    const statArticles = document.getElementById("statArticles");
    const statTopics = document.getElementById("statTopics");
    const statPositive = document.getElementById("statPositive");
    const statLatest = document.getElementById("statLatest");
    const chatFab = document.getElementById("chatFab");
    const chatOverlay = document.getElementById("chatOverlay");
    const chatPanel = document.getElementById("chatPanel");
    const chatCloseBtn = document.getElementById("chatCloseBtn");
    const chatMessages = document.getElementById("chatMessages");
    const suggestionChips = document.getElementById("suggestionChips");
    const quickBriefingBtn = document.getElementById("quickBriefingBtn");
    const chatInput = document.getElementById("chatInput");
    const chatSendBtn = document.getElementById("chatSendBtn");
    const deskSection = document.getElementById("desk");
    const editionStage = document.getElementById("editionStage");
    const heroVisuals = document.getElementById("heroVisuals");
    const heroBlankStack = document.getElementById("heroBlankStack");
    const heroSynthesisProgress = document.getElementById("heroSynthesisProgress");
    const synthesisProgressMessage = document.getElementById("synthesisProgressMessage");
    const cancelRequestBtn = document.getElementById("cancelRequestBtn");
    const wordcloudFrame = document.getElementById("wordcloudFrame");
    const THEME_STORAGE_KEY = "veritas-theme";
    let synthesisMessageTimer = null;
    let synthesisMessageIndex = 0;
    let synthesisMessages = [];
    let activeFetchController = null;
    let activeFetchReset = null;

    function escapeHtml(value) {
      return String(value ?? "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
    }

    function cleanText(value) {
      return String(value ?? "").replace(/\s+/g, " ").trim();
    }

    function delay(ms) {
      return new Promise((resolve) => window.setTimeout(resolve, ms));
    }

    function safeUrl(value) {
      try {
        const url = new URL(String(value || ""));
        if (url.protocol === "http:" || url.protocol === "https:") return url.href;
      } catch (_error) {}
      return "#";
    }

    async function postJSON(url, body, options = {}) {
      const response = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body || {}),
        signal: options.signal
      });

      if (!response.ok) {
        let detail = "Request failed";
        try {
          detail = await response.text();
        } catch (_error) {}
        const error = new Error(detail || "Request failed");
        error.status = response.status;
        throw error;
      }

      return response.json();
    }

    async function warmBackend(force = false) {
      if (backendWarmupPromise && !force) return backendWarmupPromise;
      backendWarmupPromise = fetch("/warmup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: "{}",
        keepalive: true
      })
        .then((response) => response.ok ? response.json().catch(() => ({})) : {})
        .catch(() => ({}));
      return backendWarmupPromise;
    }

    function themeToken(name, fallback) {
      const value = getComputedStyle(document.body).getPropertyValue(name).trim();
      return value || fallback;
    }

    function chartThemeTokens() {
      const isDark = document.body.dataset.theme === "dark";
      return {
        font: themeToken("--text-color", isDark ? "#F5F5F5" : "#1A1A1A"),
        legend: themeToken("--chart-legend", isDark ? "#D8E0DA" : "#1A1A1A"),
        grid: themeToken("--chart-grid", isDark ? "rgba(219, 231, 223, 0.10)" : "rgba(0, 0, 0, 0.10)"),
        zero: themeToken("--chart-zero", isDark ? "rgba(219, 231, 223, 0.18)" : "rgba(0, 0, 0, 0.16)"),
        band: themeToken("--chart-band", isDark ? "rgba(45, 138, 112, 0.18)" : "rgba(45, 138, 112, 0.10)"),
        marker: themeToken("--chart-marker", isDark ? "rgba(102, 179, 151, 0.76)" : "rgba(33, 94, 70, 0.72)"),
        markerLine: themeToken("--chart-marker-line", isDark ? "rgba(15, 21, 17, 0.92)" : "rgba(255,255,255,0.92)"),
        axis: themeToken("--text-color", isDark ? "#F5F5F5" : "#1A1A1A"),
        hoverBg: isDark ? "#1E1E1E" : "#FFFFFF",
        hoverBorder: isDark ? "rgba(255, 255, 255, 0.08)" : "rgba(23, 33, 25, 0.08)"
      };
    }

    function preferredTheme() {
      try {
        const stored = window.localStorage.getItem(THEME_STORAGE_KEY);
        if (stored === "light" || stored === "dark") return stored;
      } catch (_error) {}
      return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    }

    function applyTheme(theme) {
      const nextTheme = theme === "dark" ? "dark" : "light";
      document.body.dataset.theme = nextTheme;
      if (themeToggle) {
        const isDark = nextTheme === "dark";
        themeToggle.textContent = isDark ? "Light Mode" : "Dark Mode";
        themeToggle.setAttribute("aria-pressed", isDark ? "true" : "false");
      }
      try {
        window.localStorage.setItem(THEME_STORAGE_KEY, nextTheme);
      } catch (_error) {}
      window.requestAnimationFrame(syncChartTheme);
    }

    function synthesisMessagesFor(language) {
      return [
        "Initializing Neural Engines...",
        "Translating Global Sources...",
        "Synthesizing Results..."
      ];
    }

    function cancelActiveRequest() {
      if (!activeFetchController) return;
      if (typeof activeFetchReset === "function") activeFetchReset();
      activeFetchController.abort();
    }

    async function fetchJSONWithRetry(url, body, timeoutMs, retry502, retryTimeout, externalSignal) {
      let attemptedRetry = false;
      let attemptedTimeoutRetry = false;
      let activeTimeoutMs = timeoutMs;
      while (true) {
        if (externalSignal && externalSignal.aborted) {
          const abortedError = new Error("aborted");
          abortedError.code = "ABORTED";
          throw abortedError;
        }
        const controller = new AbortController();
        const relayAbort = () => controller.abort();
        if (externalSignal) externalSignal.addEventListener("abort", relayAbort, { once: true });
        const timer = window.setTimeout(() => controller.abort(), activeTimeoutMs);
        try {
          const response = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body || {}),
            signal: controller.signal
          });

          if (response.status === 502 && retry502 && !attemptedRetry) {
            attemptedRetry = true;
            setStatus("Tunnel warming up. Retrying once automatically...", false);
            await warmBackend(true);
            await delay(900);
            continue;
          }

          if (!response.ok) {
            const detail = await response.text().catch(() => "Request failed");
            const error = new Error(detail || "Request failed");
            error.status = response.status;
            throw error;
          }

          return response.json();
        } catch (error) {
          if (externalSignal && externalSignal.aborted) {
            const abortedError = new Error("aborted");
            abortedError.code = "ABORTED";
            throw abortedError;
          }
          if (error.name === "AbortError") {
            if (retryTimeout && !attemptedTimeoutRetry) {
              attemptedTimeoutRetry = true;
              activeTimeoutMs = Math.max(activeTimeoutMs, 45000);
              setStatus("First load is warming the research engine. Holding the connection a little longer...", false);
              await warmBackend(true);
              await delay(1200);
              continue;
            }
            const timeoutError = new Error("timeout");
            timeoutError.code = "TIMEOUT";
            throw timeoutError;
          }
          if (error.status === 502 && retry502 && !attemptedRetry) {
            attemptedRetry = true;
            setStatus("Tunnel warming up. Retrying once automatically...", false);
            await warmBackend(true);
            await delay(900);
            continue;
          }
          throw error;
        } finally {
          window.clearTimeout(timer);
          if (externalSignal) externalSignal.removeEventListener("abort", relayAbort);
        }
      }
    }

    function sourceFor(article) {
      return cleanText(article && article.source) || "Unknown Source";
    }

    function topicFor(article) {
      return cleanText(article && article.topic) || "General";
    }

    function publishedFor(article) {
      return cleanText(article && article.published_display) || "Latest";
    }

    function articleDateFor(article) {
      const candidates = [
        article && article.published_at,
        article && article.published,
        article && article.pubDate,
        article && article.published_display
      ];

      for (const candidate of candidates) {
        const value = cleanText(candidate);
        if (!value) continue;
        const date = new Date(value);
        if (!Number.isNaN(date.getTime())) return date;
      }

      return null;
    }

    function relativeTimeFromDate(date, fallback) {
      if (!(date instanceof Date) || Number.isNaN(date.getTime())) return cleanText(fallback) || "Live";
      const diff = Date.now() - date.getTime();
      if (!Number.isFinite(diff) || diff < 0) return cleanText(fallback) || "Live";

      const minute = 60 * 1000;
      const hour = 60 * minute;
      const day = 24 * hour;

      if (diff < minute) return "Just now";
      if (diff < hour) return `${Math.max(1, Math.floor(diff / minute))}m ago`;
      if (diff < day) return `${Math.max(1, Math.floor(diff / hour))}h ago`;
      return `${Math.max(1, Math.floor(diff / day))}d ago`;
    }

    function relativeTimeFor(article) {
      const date = articleDateFor(article);
      return relativeTimeFromDate(date, publishedFor(article));
    }

    function headlineFor(article) {
      return cleanText(article && (article.translated_headline || article.headline));
    }

    function summaryFor(article, limit) {
      const text = cleanText(article && (article.summary || article.headline || article.translated_headline));
      if (!text) return "";
      if (text.length <= limit) return text;
      return `${text.slice(0, Math.max(limit - 1, 0)).trimEnd()}...`;
    }

    function filteredArticles(articles) {
      return (articles || []).filter((article) => safeUrl(article && article.link) !== "#" && headlineFor(article));
    }

    function sentimentKey(sentiment) {
      const value = cleanText(sentiment).toLowerCase();
      if (value === "positive") return "positive";
      if (value === "negative") return "negative";
      return "neutral";
    }

    function sentimentLabel(sentiment) {
      const key = sentimentKey(sentiment);
      return key.charAt(0).toUpperCase() + key.slice(1);
    }

    function sentimentBadgeMarkup(sentiment) {
      const key = sentimentKey(sentiment);
      return `<span class="sentiment ${key}">${escapeHtml(sentimentLabel(sentiment))}</span>`;
    }

    function readingTimeFor(article) {
      const content = `${headlineFor(article)} ${summaryFor(article, 280)}`.trim();
      const words = content.split(/\s+/).filter(Boolean).length || 1;
      return `Reading Time: ${Math.max(1, Math.ceil(words / 220))} min`;
    }

    function sourceReliabilityFor(source) {
      const normalized = cleanText(source).toLowerCase();
      const match = RELIABLE_SOURCES.some((item) => normalized.includes(item.toLowerCase()));
      return match ? "Source Reliability: High" : "Source Reliability: Tracked";
    }

    function setStatus(message, isError) {
      statusLine.textContent = cleanText(message);
      statusLine.classList.toggle("is-error", Boolean(isError));
    }

    function setFetchLoading(isLoading) {
      fetchBtn.classList.toggle("is-loading", Boolean(isLoading));
      heroFetchBtn.classList.toggle("is-loading", Boolean(isLoading));
      sampleBtn.classList.toggle("is-loading", Boolean(isLoading));
      fetchBtn.textContent = isLoading ? "Fetching..." : "Fetch News";
      heroFetchBtn.textContent = isLoading ? "Building..." : "Build Live Edition";
      fetchBtn.disabled = Boolean(isLoading);
      heroFetchBtn.disabled = Boolean(isLoading);
      sampleBtn.disabled = Boolean(isLoading);
      languageSelect.disabled = Boolean(isLoading);
      topicInputs.forEach((input) => { input.disabled = Boolean(isLoading); });
    }

    function setSynthesisProgress(isVisible, language) {
      if (!heroBlankStack || !heroSynthesisProgress || !synthesisProgressMessage) return;
      window.clearInterval(synthesisMessageTimer);
      synthesisMessageTimer = null;

      if (isVisible) {
        synthesisMessages = synthesisMessagesFor(language);
        synthesisMessageIndex = 0;
        synthesisProgressMessage.textContent = synthesisMessages[synthesisMessageIndex];
        heroBlankStack.hidden = true;
        heroSynthesisProgress.hidden = false;
        if (heroVisuals) heroVisuals.classList.add("is-synthesizing");
        synthesisMessageTimer = window.setInterval(() => {
          synthesisMessageIndex = (synthesisMessageIndex + 1) % synthesisMessages.length;
          synthesisProgressMessage.textContent = synthesisMessages[synthesisMessageIndex];
        }, 12000);
        return;
      }

      heroSynthesisProgress.hidden = true;
      heroBlankStack.hidden = false;
      if (heroVisuals) heroVisuals.classList.remove("is-synthesizing");
      synthesisMessageIndex = 0;
      synthesisMessages = synthesisMessagesFor(languageSelect ? languageSelect.value : "English");
      synthesisProgressMessage.textContent = synthesisMessages[0];
    }

    function setChatLoading(isLoading) {
      chatSendBtn.classList.toggle("is-loading", Boolean(isLoading));
      chatSendBtn.textContent = isLoading ? "Sending..." : "Ask";
      chatSendBtn.disabled = Boolean(isLoading);
      quickBriefingBtn.disabled = Boolean(isLoading);
      chatInput.disabled = Boolean(isLoading);
    }

    function metaDotMarkup() {
      return '<span class="meta-dot" aria-hidden="true"></span>';
    }

    function updateCoverageCount(count) {
      if (count > 0) {
        coverageCount.textContent = `${count} stories`;
        coverageCount.classList.add("is-visible");
      } else {
        coverageCount.textContent = "";
        coverageCount.classList.remove("is-visible");
      }
    }

    function quietFeatureMarkup() {
      return `
        <div class="quiet-card">
          <div class="quiet-panel">
            <div>
              <span class="quiet-kicker">Edition Preview</span>
              <h3 class="quiet-title">The first fetch turns this into a composed lead story.</h3>
              <p class="quiet-copy">Use the desk above to build a calmer front page with a lead article, a side rail, deeper coverage, visuals, and a reasoning trace.</p>
            </div>
          </div>
        </div>
      `;
    }

    function previewHeroCardsMarkup() {
      return `
        <article class="blank-card blank-card--one">
          <div class="blank-card-top">
            <span class="blank-pill short"></span>
            <div class="blank-chip-row">
              <span class="blank-chip"></span>
              <span class="blank-chip"></span>
            </div>
          </div>
          <div class="blank-line xl"></div>
          <div class="blank-line lg"></div>
          <div class="blank-line md"></div>
          <div class="blank-card-frame">
            <div class="blank-card-box"></div>
            <div class="blank-card-box"></div>
          </div>
        </article>
        <article class="blank-card blank-card--two">
          <div class="blank-card-top">
            <span class="blank-pill mid"></span>
            <div class="blank-chip-row">
              <span class="blank-chip"></span>
              <span class="blank-chip"></span>
              <span class="blank-chip"></span>
            </div>
          </div>
          <div class="blank-line xl"></div>
          <div class="blank-line lg"></div>
          <div class="blank-line sm"></div>
          <div class="blank-card-footer">
            <span class="blank-card-dot"></span>
            <div class="blank-line md"></div>
          </div>
        </article>
        <article class="blank-card blank-card--three">
          <div class="blank-card-top">
            <span class="blank-pill long"></span>
            <div class="blank-chip-row">
              <span class="blank-chip"></span>
              <span class="blank-chip"></span>
            </div>
          </div>
          <div class="blank-line xl"></div>
          <div class="blank-line lg"></div>
          <div class="blank-line md"></div>
          <div class="blank-line sm"></div>
          <div class="blank-card-frame">
            <div class="blank-card-box"></div>
            <div class="blank-card-box"></div>
          </div>
          <div class="blank-card-footer">
            <span class="blank-card-dot"></span>
            <div class="blank-line lg"></div>
          </div>
        </article>
      `;
    }

    function editionTimestamp(date = new Date()) {
      try {
        return new Intl.DateTimeFormat(undefined, {
          month: "short",
          day: "numeric",
          hour: "numeric",
          minute: "2-digit"
        }).format(date);
      } catch (_error) {
        return cleanText(date && date.toString()) || "Now";
      }
    }

    function extractHeroCategories(articles, topics) {
      const values = [];
      (articles || []).forEach((article) => {
        const direct = [
          cleanText(article && article.category),
          cleanText(article && article.section),
          cleanText(article && article.topic)
        ].filter(Boolean);
        const multi = Array.isArray(article && article.categories)
          ? article.categories.map((value) => cleanText(value)).filter(Boolean)
          : [];
        [...direct, ...multi].forEach((value) => {
          if (value && !values.includes(value)) values.push(value);
        });
      });

      (topics || []).map((value) => cleanText(value)).filter(Boolean).forEach((value) => {
        if (!values.includes(value)) values.push(value);
      });

      return values.slice(0, 3);
    }

    function liveHeroCardsMarkup(articles, topics, createdAt) {
      const items = filteredArticles(articles);
      const lead = items[0] || {};
      const categories = extractHeroCategories(items, topics);
      const categoryList = categories.length ? categories : ["General"];
      const articleCount = items.length;
      const stamp = editionTimestamp(createdAt);

      return `
        <article class="blank-card blank-card--one is-live">
          <div class="hero-card-shell">
            <div class="hero-card-meta">
              <span class="hero-card-kicker">Edition Ledger</span>
              <span class="hero-card-stamp">${escapeHtml(sourceFor(lead) || "Live Desk")}</span>
            </div>
            <div class="hero-card-stat-grid">
              <div class="hero-card-stat">
                <p class="hero-card-stat-label">Stories</p>
                <p class="hero-card-stat-value">${escapeHtml(String(articleCount || 0))}</p>
                <p class="hero-card-stat-copy">Stories accepted into the current edition.</p>
              </div>
              <div class="hero-card-stat">
                <p class="hero-card-stat-label">Edition Time</p>
                <p class="hero-card-stat-value">${escapeHtml(stamp)}</p>
                <p class="hero-card-stat-copy">Timestamp when this edition card deck resolved.</p>
              </div>
            </div>
            <p class="hero-card-note">The full coverage grid below expands this count into a source-by-source reading path.</p>
          </div>
        </article>
        <article class="blank-card blank-card--two is-live">
          <div class="hero-card-shell">
            <div class="hero-card-meta">
              <span class="hero-card-kicker">Edition Signals</span>
              <span class="hero-card-stamp">${escapeHtml(stamp)}</span>
            </div>
            <div class="hero-card-list">
              <p class="hero-card-list-label">Categories</p>
              <div class="hero-card-badge-row">
                ${categoryList.map((category) => `<span class="hero-card-badge">${escapeHtml(category)}</span>`).join("")}
              </div>
            </div>
            <p class="hero-card-note">Three live angles pulled from the fetched JSON are pinned here to frame the edition before you move into the full desk.</p>
          </div>
        </article>
        <article class="blank-card blank-card--three is-live">
          <div class="hero-card-shell">
            <div class="hero-card-meta">
              <span class="hero-card-kicker">Front Page</span>
              <span class="hero-card-stamp">${escapeHtml(relativeTimeFor(lead))}</span>
            </div>
            <div>
              <h3 class="hero-card-title">${escapeHtml(headlineFor(lead) || "Live edition ready")}</h3>
              <p class="hero-card-summary">${escapeHtml(summaryFor(lead, 250) || "The current lead story is now surfaced and ready to read in the main edition below.")}</p>
            </div>
            <div class="hero-card-footer">
              <p class="hero-card-caption">The lead story below anchors the full edition, with the rail and coverage grid continuing the briefing.</p>
              <button class="hero-card-arrow" id="heroEditionArrow" type="button" aria-label="Scroll to more news">
                <svg viewBox="0 0 24 24" aria-hidden="true">
                  <path d="M12 5v14"></path>
                  <path d="m6 13 6 6 6-6"></path>
                </svg>
              </button>
            </div>
          </div>
        </article>
      `;
    }

    function renderHeroPreviewCards() {
      if (!heroBlankStack) return;
      heroBlankStack.classList.remove("is-loaded");
      heroBlankStack.innerHTML = previewHeroCardsMarkup();
    }

    function renderHeroEditionCards(articles, topics, options = {}) {
      if (!heroBlankStack) return;
      const items = filteredArticles(articles);
      if (!items.length) {
        renderHeroPreviewCards();
        return;
      }

      const animate = options.animate !== false;
      heroBlankStack.classList.remove("is-loaded");
      heroBlankStack.innerHTML = liveHeroCardsMarkup(items, topics || currentTopics, options.createdAt || new Date());
      if (!animate) {
        heroBlankStack.classList.add("is-loaded");
        return;
      }
      window.requestAnimationFrame(() => {
        window.requestAnimationFrame(() => heroBlankStack.classList.add("is-loaded"));
      });
    }

    function quietRailMarkup() {
      const rows = [
        { title: "Secondary stories appear here after the first fetch." },
        { title: "Each item keeps only source, time, headline, and summary." },
        { title: "More stories continue below in the coverage grid." }
      ];

      return `
        <div class="quiet-rail">
          ${rows.map((row) => `
            <div class="quiet-rail-row">
              <div class="quiet-title-small">${escapeHtml(row.title)}</div>
            </div>
          `).join("")}
        </div>
      `;
    }

    function quietCoverageMarkup() {
      const slots = [
        "Global Perspective: Cross-references international wires to identify localized impacts of global trends.",
        "Temporal Analysis: Tracks how storylines have evolved over the last 24 hours to separate breaking news from noise.",
        "Source Integrity: Weights reporting based on historical accuracy and publisher bias metrics."
      ];

      return slots.map((copy) => `
        <article class="surface interactive coverage-card">
          <p class="coverage-summary">${escapeHtml(copy)}</p>
        </article>
      `).join("");
    }

    function connectionRetryMarkup() {
      return `
        <div class="quiet-card">
          <div class="quiet-panel">
            <div>
              <span class="quiet-kicker">Connection Refined</span>
              <h3 class="quiet-title">Connection Refined - Please Retry</h3>
              <p class="quiet-copy">The desk could not complete this pass. Please retry once the connection settles.</p>
            </div>
          </div>
        </div>
      `;
    }

    function deferredFeatureMarkup() {
      return `
        <div class="quiet-card">
          <div class="quiet-panel">
            <div>
              <span class="quiet-kicker">Warming Up</span>
              <h3 class="quiet-title">The desk is still assembling the current edition.</h3>
              <p class="quiet-copy">This topic mix is taking longer than usual to resolve. Retry in a few seconds or narrow the topic set for a faster first pass.</p>
            </div>
          </div>
        </div>
      `;
    }

    function renderDeferredState() {
      heroArticle.innerHTML = deferredFeatureMarkup();
      secondaryArticles.innerHTML = quietRailMarkup();
      trendingSection.classList.remove("is-visible");
      trendingSources.innerHTML = "";
      coverageGrid.innerHTML = quietCoverageMarkup();
      updateCoverageCount(0);
    }

    function renderConnectionRetryState() {
      heroArticle.innerHTML = connectionRetryMarkup();
      secondaryArticles.innerHTML = quietRailMarkup();
      trendingSection.classList.remove("is-visible");
      trendingSources.innerHTML = "";
      coverageGrid.innerHTML = quietCoverageMarkup();
      updateCoverageCount(0);
    }

    function loadingFeatureMarkup() {
      return `
        <div class="loading-lead">
          <div class="loading-lead-copy">
            <div class="skeleton-meta">
              <div class="skeleton-pill wide"></div>
              <div class="skeleton-pill mid"></div>
              <div class="skeleton-pill wide"></div>
            </div>
            <div class="skeleton-line xl"></div>
            <div class="skeleton-line lg"></div>
            <div class="skeleton-meta">
              <div class="skeleton-pill wide"></div>
              <div class="skeleton-pill wide"></div>
              <div class="skeleton-pill mid"></div>
            </div>
            <div class="skeleton-line md"></div>
            <div class="skeleton-line sm"></div>
          </div>
        </div>
      `;
    }

    function loadingRailMarkup() {
      return `
        <div class="loading-rail">
          ${Array.from({ length: 4 }).map((_, index) => `
            <div class="loading-rail-row">
              <div class="skeleton-meta">
                <div class="skeleton-pill wide"></div>
                <div class="skeleton-pill mid"></div>
                <div class="skeleton-pill mid"></div>
              </div>
              <div class="skeleton-line ${index % 2 === 0 ? "lg" : "md"}"></div>
              <div class="skeleton-line sm"></div>
            </div>
          `).join("")}
        </div>
      `;
    }

    function loadingCoverageMarkup() {
      return Array.from({ length: 3 }).map(() => `
        <article class="surface loading-coverage">
          <div class="skeleton-meta">
            <div class="skeleton-pill wide"></div>
            <div class="skeleton-pill mid"></div>
          </div>
          <div class="skeleton-line xl"></div>
          <div class="skeleton-line lg"></div>
          <div class="skeleton-line md"></div>
          <div class="skeleton-line sm"></div>
        </article>
      `).join("");
    }

    function renderQuietState() {
      heroArticle.innerHTML = quietFeatureMarkup();
      secondaryArticles.innerHTML = quietRailMarkup();
      trendingSection.classList.remove("is-visible");
      trendingSources.innerHTML = "";
      coverageGrid.innerHTML = quietCoverageMarkup();
      updateCoverageCount(0);
    }

    function renderLoadingState() {
      heroArticle.innerHTML = loadingFeatureMarkup();
      secondaryArticles.innerHTML = loadingRailMarkup();
      trendingSection.classList.remove("is-visible");
      trendingSources.innerHTML = "";
      coverageGrid.innerHTML = loadingCoverageMarkup();
      updateCoverageCount(0);
    }

    function renderLeadArticle(article) {
      heroArticle.innerHTML = `
        <div class="story-card news-card">
          <div class="lead-story-layout">
            <div class="lead-story-copy">
              <div class="lead-kicker">
                <div class="lead-kicker-left">
                  <span class="meta-pill">${escapeHtml(sourceFor(article))}</span>
                  <span class="meta-pill">${escapeHtml(topicFor(article))}</span>
                </div>
              </div>
              <div class="lead-body">
                <p class="lead-overline">${escapeHtml(relativeTimeFor(article))} ${metaDotMarkup()} ${escapeHtml(publishedFor(article))}</p>
                <h2 class="lead-headline">
                  <a href="${escapeHtml(safeUrl(article.link))}" target="_blank" rel="noopener noreferrer">${escapeHtml(headlineFor(article))}</a>
                </h2>
                <div class="lead-facts">
                  <span class="lead-fact">${escapeHtml(readingTimeFor(article))}</span>
                  <span class="lead-fact">${escapeHtml(sourceReliabilityFor(sourceFor(article)))}</span>
                  ${sentimentBadgeMarkup(article.sentiment)}
                </div>
                <p class="lead-summary">${escapeHtml(summaryFor(article, 360))}</p>
              </div>
              <div class="lead-note">
                This lead story is the anchor for the current edition. Open the full article for source context, then use the assistant for follow-up synthesis.
              </div>
            </div>
          </div>
        </div>
      `;
    }

    function renderRailArticles(articles) {
      const items = filteredArticles(articles).slice(0, 5);
      if (!items.length) {
        secondaryArticles.innerHTML = quietRailMarkup();
        return;
      }

      secondaryArticles.innerHTML = `
        ${items.map((article, index) => `
        <article class="rail-item news-card" style="animation-delay:${index * 70}ms;">
          <div class="rail-body">
            <div class="rail-topline">
              <div class="rail-meta">
                <span class="rail-source">${escapeHtml(sourceFor(article))}</span>
                ${metaDotMarkup()}
                <span>${escapeHtml(relativeTimeFor(article))}</span>
              </div>
            </div>
            <div class="rail-meta">
              <span>${escapeHtml(topicFor(article))}</span>
              ${sentimentBadgeMarkup(article.sentiment)}
            </div>
            <h3 class="rail-headline">
              <a href="${escapeHtml(safeUrl(article.link))}" target="_blank" rel="noopener noreferrer">${escapeHtml(headlineFor(article))}</a>
            </h3>
            <div class="rail-summary">${escapeHtml(summaryFor(article, 120))}</div>
          </div>
        </article>
      `).join("")}
      `;
    }

    function renderTrendingSources(articles) {
      const unique = [];
      filteredArticles(articles).forEach((article) => {
        const source = sourceFor(article);
        if (source && !unique.includes(source)) unique.push(source);
      });

      if (!unique.length) {
        trendingSection.classList.remove("is-visible");
        trendingSources.innerHTML = "";
        return;
      }

      trendingSection.classList.add("is-visible");
      trendingSources.innerHTML = unique.slice(0, 12).map((source) => `
        <span class="trending-pill">${escapeHtml(source)}</span>
      `).join("");
    }

    function renderCoverage(articles) {
      const items = filteredArticles(articles).slice(6);
      if (!items.length) {
        coverageGrid.innerHTML = quietCoverageMarkup();
        updateCoverageCount(0);
        return;
      }

      updateCoverageCount(items.length);
      coverageGrid.innerHTML = items.map((article, index) => `
        <article class="surface interactive coverage-card news-card" style="animation-delay:${index * 60}ms;">
          <div class="coverage-meta">
            <span class="coverage-source">${escapeHtml(sourceFor(article))}</span>
            ${sentimentBadgeMarkup(article.sentiment)}
            ${metaDotMarkup()}
            <span>${escapeHtml(relativeTimeFor(article))}</span>
          </div>
          <h3 class="coverage-headline">
            <a href="${escapeHtml(safeUrl(article.link))}" target="_blank" rel="noopener noreferrer">${escapeHtml(headlineFor(article))}</a>
          </h3>
          <p class="coverage-summary">${escapeHtml(summaryFor(article, 160))}</p>
          <a class="coverage-link" href="${escapeHtml(safeUrl(article.link))}" target="_blank" rel="noopener noreferrer">Read more</a>
        </article>
      `).join("");
    }

    function renderArticles(articles) {
      const items = filteredArticles(articles);
      if (!items.length) {
        renderQuietState();
        return;
      }

      renderLeadArticle(items[0]);
      renderRailArticles(items.slice(1, 6));
      renderTrendingSources(items);
      renderCoverage(items);
    }

    function renderTicker(articles) {
      const items = filteredArticles(articles).slice(0, 10).map((article) => ({
        topic: topicFor(article),
        headline: headlineFor(article)
      }));
      const payload = items.length ? items : DEFAULT_TICKER;
      const markup = payload.map((item) => `
        <span class="ticker-item">
          <strong>${escapeHtml(item.topic)}</strong>
          <span>${escapeHtml(item.headline)}</span>
        </span>
      `).join("");
      tickerTrack.innerHTML = markup + markup;
    }

    function renderBriefing(briefing, topics) {
      const cleanBrief = cleanText(briefing);
      if (!cleanBrief) {
        briefCard.hidden = true;
        briefCard.classList.remove("is-visible");
        briefText.textContent = "";
        briefTopics.innerHTML = "";
        return;
      }

      briefCard.hidden = false;
      briefCard.classList.add("is-visible");
      briefText.textContent = cleanBrief;
      briefTopics.innerHTML = (topics || []).filter(Boolean).map((topic) => `
        <span class="brief-topic">${escapeHtml(cleanText(topic))}</span>
      `).join("");
    }

    function clearVisualFrames() {
      if (wordcloudFrame) {
        wordcloudFrame.innerHTML = '<div class="wordcloud-stage is-loading"></div>';
      }
      ["pie-chart", "bar-chart", "scatter-chart"].forEach((id) => {
        const el = document.getElementById(id);
        if (!el) return;
        if (typeof Plotly !== "undefined") {
          try { Plotly.purge(el); } catch (_error) {}
        }
        el.innerHTML = '<div class="visual-empty"></div>';
      });
    }

    function toDateValue(value) {
      const date = value instanceof Date ? value : new Date(value);
      return Number.isNaN(date.getTime()) ? null : date;
    }

    function gradientPalette(length) {
      const start = [33, 94, 70];
      const end = [98, 111, 125];
      const total = Math.max(length - 1, 1);
      return Array.from({ length: Math.max(length, 1) }).map((_, index) => {
        const ratio = index / total;
        const rgb = start.map((channel, i) => Math.round(channel + ((end[i] - channel) * ratio)));
        return `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;
      });
    }

    function relativeTickConfig(values, tickColor) {
      const parsed = (values || []).map((value) => ({ raw: value, date: toDateValue(value) })).filter((item) => item.date);
      return {
        showticklabels: false,
        tickfont: { color: tickColor || "#1A1A1A", size: 11 },
        ticklabeloverflow: "hide past domain",
        automargin: true
      };
    }

    function scatterThemeShapes(_theme) {
      return [];
    }

    function scrubPlotlySurface(el) {
      if (!el) return;
      el.style.background = "transparent";
      const selectors = [
        ".bg",
        ".plotbg",
        ".bglayer rect",
        ".cartesianlayer .subplot rect.bg",
        ".main-svg rect.bg",
        ".main-svg",
        ".svg-container",
        ".plot-container"
      ];
      el.querySelectorAll(selectors.join(",")).forEach((node) => {
        if (node instanceof SVGElement) {
          node.setAttribute("fill", "transparent");
          node.setAttribute("stroke", "transparent");
        }
        if (node.style) {
          node.style.background = "transparent";
          node.style.fill = "transparent";
          node.style.stroke = "transparent";
          node.style.boxShadow = "none";
        }
      });
    }

    function syncChartTheme() {
      if (typeof Plotly === "undefined") return;
      const theme = chartThemeTokens();
      const commonLayout = {
        paper_bgcolor: "rgba(0,0,0,0)",
        plot_bgcolor: "rgba(0,0,0,0)",
        font: { family: "Inter, sans-serif", size: 11, color: theme.font },
        legend: {
          bgcolor: "rgba(0,0,0,0)",
          font: { family: "Inter, sans-serif", size: 12, color: theme.legend }
        }
      };

      const pieChart = document.getElementById("pie-chart");
      if (pieChart && Array.isArray(pieChart.data) && pieChart.data.length) {
        Plotly.restyle(pieChart, {
          textinfo: "percent+label",
          textposition: "inside",
          insidetextfont: [{ color: "#FFFFFF", family: "Inter, sans-serif", size: 16 }],
          textfont: [{ color: "#FFFFFF", family: "Inter, sans-serif", size: 16 }],
          hoverlabel: [{
            bgcolor: theme.hoverBg,
            bordercolor: theme.hoverBorder,
            font: { color: theme.font, family: "Inter, sans-serif" }
          }]
        }).catch(() => {});
        Plotly.relayout(pieChart, Object.assign({}, commonLayout, {
          automargin: false,
          margin: { t: 0, b: 0, l: 0, r: 0 },
          showlegend: true,
          legend: {
            x: 1,
            y: 0.5,
            xanchor: "left",
            yanchor: "middle",
            orientation: "v",
            bgcolor: "rgba(0,0,0,0)",
            font: { family: "Inter, sans-serif", size: 12, color: theme.legend }
          },
          uniformtext: { minsize: 12, mode: "hide" }
        })).then(() => scrubPlotlySurface(pieChart)).catch(() => {});
      }

      const barChart = document.getElementById("bar-chart");
      if (barChart && Array.isArray(barChart.data) && barChart.data.length) {
        Plotly.relayout(barChart, Object.assign({}, commonLayout, {
          margin: { t: 0, b: 0, l: 0, r: 0 },
          xaxis: Object.assign({}, barChart.layout && barChart.layout.xaxis ? barChart.layout.xaxis : {}, {
            showgrid: true,
            gridcolor: theme.grid,
            zeroline: false,
            color: theme.font,
            tickfont: { color: theme.font, size: 11 },
            title: ""
          }),
          yaxis: Object.assign({}, barChart.layout && barChart.layout.yaxis ? barChart.layout.yaxis : {}, {
            showgrid: false,
            color: theme.font,
            tickfont: { color: theme.font, size: 11 },
            title: ""
          })
        })).then(() => scrubPlotlySurface(barChart)).catch(() => {});
      }

      const scatterChart = document.getElementById("scatter-chart");
      if (scatterChart && Array.isArray(scatterChart.data) && scatterChart.data.length) {
        const scatterXValues = Array.isArray(scatterChart.data[0] && scatterChart.data[0].x) ? scatterChart.data[0].x : [];
        Plotly.restyle(scatterChart, {
          "marker.color": theme.marker,
          "marker.line.color": theme.markerLine
        }).catch(() => {});
        Plotly.relayout(scatterChart, Object.assign({}, commonLayout, {
          margin: { t: 0, b: 0, l: 0, r: 0 },
          xaxis: Object.assign(
            {},
            scatterChart.layout && scatterChart.layout.xaxis ? scatterChart.layout.xaxis : {},
            relativeTickConfig(scatterXValues, theme.font),
            {
              title: "",
              showgrid: true,
              gridcolor: theme.grid,
              zeroline: false,
              color: theme.font,
              tickfont: { color: theme.font, size: 11 }
            }
          ),
          yaxis: Object.assign({}, scatterChart.layout && scatterChart.layout.yaxis ? scatterChart.layout.yaxis : {}, {
            title: "",
            showgrid: true,
            gridcolor: theme.grid,
            zeroline: false,
            color: theme.font,
            tickfont: { color: theme.font, size: 11 }
          }),
          shapes: scatterThemeShapes(theme)
        })).then(() => scrubPlotlySurface(scatterChart)).catch(() => {});
      }
    }

    function renderWordcloud(dataUrl) {
      if (!wordcloudFrame) return;
      if (!cleanText(dataUrl)) {
        wordcloudFrame.innerHTML = '<div class="wordcloud-stage is-loading"></div>';
        return;
      }

      wordcloudFrame.innerHTML = `<div class="wordcloud-stage"><img class="wordcloud-image" src="${escapeHtml(dataUrl)}" alt="Word cloud visualization" /></div>`;
    }

    async function loadVisuals(retry = true) {
      if (!originalArticles.length) return;
      if (typeof Plotly === "undefined") {
        if (retry) setTimeout(() => loadVisuals(false), 500);
        return;
      }
      try {
        const theme = chartThemeTokens();
        const res = await fetch("/visuals", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ articles: originalArticles })
        });
        const data = await res.json();

        renderWordcloud(data.wordcloud || "");

        const chartConfigs = [
          { key: "pie", id: "pie-chart" },
          { key: "bar", id: "bar-chart" },
          { key: "scatter", id: "scatter-chart" }
        ];

        for (const cfg of chartConfigs) {
          const figure = data[cfg.key];
          const el = document.getElementById(cfg.id);
          if (!figure || !el) continue;

          let fig = typeof figure === "string" ? JSON.parse(figure) : figure;
          const greenPalette = ["#1D5640", "#2A7255", "#418A6D", "#5BA286", "#86B8A2"];

          if (cfg.key === "pie" && Array.isArray(fig.data)) {
            const pieColorMap = {
              positive: "#356746",
              negative: "#B25755",
              neutral: "#708090"
            };
            fig = Object.assign({}, fig, {
              data: fig.data.map((trace) => Object.assign({}, trace, {
                marker: Object.assign({}, trace.marker || {}, {
                  colors: Array.isArray(trace.labels)
                    ? trace.labels.map((label) => {
                        const key = cleanText(label).toLowerCase();
                        return pieColorMap[key] || "#708090";
                      })
                    : ["#356746", "#B25755", "#708090"],
                  line: { color: "rgba(255,255,255,0.9)", width: 1.2 }
                }),
                sort: false,
                automargin: true,
                textinfo: "percent+label",
                textposition: "inside",
                insidetextorientation: "auto",
                insidetextfont: { color: "#FFFFFF", family: "Inter, sans-serif", size: 16 },
                textfont: { color: "#FFFFFF", family: "Inter, sans-serif", size: 16 },
                hoverlabel: { bgcolor: theme.hoverBg, bordercolor: theme.hoverBorder, font: { color: theme.font, family: "Inter, sans-serif" } }
              }))
            });
          }

          if (cfg.key === "bar" && Array.isArray(fig.data)) {
            const shades = gradientPalette(Array.isArray(fig.data[0] && fig.data[0].y) ? fig.data[0].y.length : 6);
            fig = Object.assign({}, fig, {
              data: fig.data.map((trace) => Object.assign({}, trace, {
                marker: Object.assign({}, trace.marker || {}, {
                  color: Array.isArray(trace.y)
                    ? trace.y.map((_, index) => shades[index % shades.length])
                    : shades[2],
                  line: { color: "rgba(255,255,255,0.9)", width: 1.2 }
                })
              }))
            });
          }

          if (cfg.key === "scatter" && Array.isArray(fig.data)) {
            fig = Object.assign({}, fig, {
              data: fig.data.map((trace) => Object.assign({}, trace, {
                customdata: Array.isArray(trace.x)
                  ? trace.x.map((value) => {
                      const date = toDateValue(value);
                      return relativeTimeFromDate(date, "Live");
                    })
                  : [],
                marker: Object.assign({}, trace.marker || {}, {
                  size: 11,
                  color: theme.marker,
                  line: { width: 1.2, color: theme.markerLine }
                }),
                hovertemplate: "%{text}<br>%{customdata}<br>Score: %{y:.2f}<extra></extra>"
              }))
            });
          }

          const layout = Object.assign({}, fig.layout || {}, {
            paper_bgcolor: "rgba(0,0,0,0)",
            plot_bgcolor: "rgba(0,0,0,0)",
            automargin: false,
            margin: { t: 0, b: 0, l: 0, r: 0 },
            font: { family: "Inter, sans-serif", size: 11, color: theme.font },
            legend: {
              bgcolor: "rgba(0,0,0,0)",
              font: { family: "Inter, sans-serif", size: 12, color: theme.legend }
            },
            title: { text: "" },
            autosize: true
          });

          if (cfg.key === "pie") {
            layout.automargin = false;
            layout.margin = { t: 0, b: 0, l: 0, r: 0 };
            layout.showlegend = true;
            layout.legend = Object.assign({}, layout.legend || {}, {
              x: 1,
              y: 0.5,
              xanchor: "left",
              yanchor: "middle",
              orientation: "v",
              bgcolor: "rgba(0,0,0,0)",
              font: { family: "Inter, sans-serif", size: 12, color: theme.legend }
            });
            layout.uniformtext = { minsize: 12, mode: "hide" };
            layout.annotations = [];
          }

          if (cfg.key === "bar") {
            layout.xaxis = Object.assign({}, layout.xaxis || {}, {
              showgrid: true,
              gridcolor: theme.grid,
              zeroline: false,
              color: theme.font,
              tickfont: { color: theme.font, size: 11 },
              title: ""
            });
            layout.yaxis = Object.assign({}, layout.yaxis || {}, {
              showgrid: false,
              color: theme.font,
              tickfont: { color: theme.font, size: 11 },
              title: ""
            });
          }

          if (cfg.key === "scatter") {
            const xValues = Array.isArray(fig.data && fig.data[0] && fig.data[0].x) ? fig.data[0].x : [];
            layout.xaxis = Object.assign({}, layout.xaxis || {}, relativeTickConfig(xValues, theme.font), {
              title: "",
              showgrid: true,
              gridcolor: theme.grid,
              zeroline: false,
              color: theme.font,
              tickfont: { color: theme.font, size: 11 }
            });
            layout.yaxis = Object.assign({}, layout.yaxis || {}, {
              title: "",
              showgrid: true,
              gridcolor: theme.grid,
              zeroline: false,
              color: theme.font,
              tickfont: { color: theme.font, size: 11 }
            });
            layout.shapes = scatterThemeShapes(theme);
          }

          Plotly.react(el, fig.data || [], layout, {
            displayModeBar: false,
            responsive: true
          }).then(() => scrubPlotlySurface(el));
        }
      } catch (error) {
        console.error("Visuals loading failed:", error);
      }
    }

    function renderAgentLog(data) {
      const topics = Object.keys(data || {});
      if (!topics.length) {
        agentLogSection.hidden = true;
        agentLogSection.classList.remove("is-visible", "is-open");
        agentLogContent.innerHTML = "";
        agentLogOpen = false;
        agentLogToggle.setAttribute("aria-expanded", "false");
        return;
      }

      agentLogSection.hidden = false;
      agentLogSection.classList.add("is-visible");
      agentLogContent.innerHTML = topics.map((topic) => {
        const entries = Array.isArray(data[topic]) ? data[topic] : [];
        return `
          <article class="surface interactive log-card">
            <h3 class="log-topic">${escapeHtml(topic)}</h3>
            ${entries.map((entry) => `
              <div class="log-entry">
                <span class="log-stage">${escapeHtml(cleanText(entry && entry.stage) || "observe")}</span>
                <div class="log-message">${escapeHtml(cleanText(entry && entry.message) || "")}</div>
              </div>
            `).join("")}
          </article>
        `;
      }).join("");
    }

    function toggleAgentLog() {
      if (agentLogSection.hidden) return;
      agentLogOpen = !agentLogOpen;
      agentLogSection.classList.toggle("is-open", agentLogOpen);
      agentLogToggle.setAttribute("aria-expanded", agentLogOpen ? "true" : "false");
    }

    function updateStatBar(data) {
      const articles = filteredArticles(data && data.articles);
      const topics = Array.isArray(data && data.topics) ? data.topics.filter(Boolean) : [];
      const positiveCount = articles.filter((article) => sentimentKey(article.sentiment) === "positive").length;
      statArticles.textContent = articles.length ? String(articles.length) : "—";
      statTopics.textContent = topics.length ? String(topics.length) : "—";
      statPositive.textContent = articles.length ? `${Math.round((positiveCount / articles.length) * 100)}%` : "—";
      statLatest.textContent = articles.length ? relativeTimeFor(articles[0]) : "—";
    }

    async function translateArticles(language, options = {}) {
      const shouldRender = options.renderOnComplete !== false;
      const requestId = ++translationRequestId;
      if (!originalArticles.length) {
        setStatus("Fetch articles before translating the edition.", true);
        return { mode: "skipped" };
      }

      if (language === "English") {
        if (requestId !== translationRequestId) return { mode: "stale" };
        const articles = [...originalArticles];
        if (shouldRender) {
          allArticles = articles;
          renderArticles(allArticles);
          renderTicker(allArticles);
        }
        return { mode: "original", articles };
      }

      try {
        const payload = await postJSON("/translate", {
          articles: originalArticles,
          language
        }, { signal: options.signal });
        if (requestId !== translationRequestId) return { mode: "stale" };
        const articles = Array.isArray(payload.articles) ? payload.articles : [...originalArticles];
        if (shouldRender) {
          allArticles = articles;
          renderArticles(allArticles);
          renderTicker(allArticles);
        }
        return { mode: "translated", articles };
      } catch (error) {
        if (error && (error.code === "ABORTED" || error.name === "AbortError")) return { mode: "aborted" };
        if (requestId !== translationRequestId) return { mode: "stale" };
        const articles = [...originalArticles];
        if (shouldRender) {
          allArticles = articles;
          renderArticles(allArticles);
          renderTicker(allArticles);
        }
        return { mode: "failed", articles };
      }
    }

    async function fetchNews(options = {}) {
      const source = cleanText(options && options.source).toLowerCase() || "desk";
      const topics = topicInputs.map((input) => cleanText(input.value)).filter(Boolean).slice(0, 3);
      if (!topics.length) {
        setStatus("Add at least one topic to build the live edition.", true);
        topicInputs[0].focus();
        return;
      }

      const snapshot = {
        originalArticles: [...originalArticles],
        allArticles: [...allArticles],
        currentTopics: [...currentTopics],
        latestBriefing,
        latestEditionTimestamp,
        reasoningData: JSON.parse(JSON.stringify(reasoningData || {}))
      };
      const requestController = new AbortController();
      let abortHandled = false;
      const restoreAfterAbort = () => {
        if (abortHandled) return;
        abortHandled = true;
        originalArticles = [];
        allArticles = [];
        currentTopics = [];
        latestBriefing = "";
        latestEditionTimestamp = null;
        reasoningData = {};
        renderQuietState();
        renderHeroPreviewCards();
        renderTicker([]);
        renderBriefing("", []);
        renderAgentLog({});
        updateStatBar({ articles: [], topics: [] });
        clearVisualFrames();
        if (resultsContainer) resultsContainer.style.display = "none";
        setStatus("Request cancelled.", false);
        setSynthesisProgress(false, languageSelect.value);
        setFetchLoading(false);
        if (activeFetchController === requestController) activeFetchController = null;
        if (activeFetchReset === restoreAfterAbort) activeFetchReset = null;
      };

      activeFetchController = requestController;
      activeFetchReset = restoreAfterAbort;
      setFetchLoading(true);
      setSynthesisProgress(true, languageSelect.value);
      setStatus("Building the live edition from live sources...", false);
      if (resultsContainer) resultsContainer.style.display = "none";
      renderLoadingState();
      renderBriefing("", []);
      renderAgentLog({});
      clearVisualFrames();
      if (source !== "hero" && editionStage) {
        window.requestAnimationFrame(() => {
          editionStage.scrollIntoView({ behavior: "smooth", block: "start" });
        });
      }

      const selectedLanguage = languageSelect.value;
      const coldStartFetch = !hasSuccessfulFetch;

      try {
        await warmBackend();
        const payload = await fetchJSONWithRetry("/fetch", { topics }, coldStartFetch ? 35000 : 22000, true, coldStartFetch, requestController.signal);
        originalArticles = Array.isArray(payload.articles) ? payload.articles : [];
        currentTopics = Array.isArray(payload.topics) && payload.topics.length ? payload.topics : topics;
        latestBriefing = cleanText(payload.briefing);
        reasoningData = payload.reasoning_log || {};
        lastTopic = currentTopics[0] || lastTopic;
        hasSuccessfulFetch = originalArticles.length > 0 || hasSuccessfulFetch;
        latestEditionTimestamp = new Date();

        if (originalArticles.length) {
          renderHeroEditionCards(originalArticles, currentTopics, {
            createdAt: latestEditionTimestamp
          });
          setSynthesisProgress(false, selectedLanguage);
        }

        let translationResult = { mode: "original" };
        if (selectedLanguage !== "English" && originalArticles.length) {
          translationResult = await translateArticles(selectedLanguage, {
            signal: requestController.signal,
            renderOnComplete: false
          });
        }

        if (!originalArticles.length) {
          setStatus("No live articles came back for those topics.", true);
          return;
        }

        if (translationResult.mode === "aborted") {
          restoreAfterAbort();
          return;
        }

        allArticles = Array.isArray(translationResult.articles) && translationResult.articles.length
          ? [...translationResult.articles]
          : [...originalArticles];

        renderHeroEditionCards(allArticles, currentTopics, {
          animate: false,
          createdAt: latestEditionTimestamp || new Date()
        });
        renderArticles(allArticles);
        renderTicker(allArticles);
        renderBriefing(latestBriefing, currentTopics);
        renderAgentLog(reasoningData);
        updateStatBar({ articles: originalArticles, topics: currentTopics });
        if (originalArticles.length) document.getElementById("results-container").style.display = "block";
        loadVisuals();

        if (translationResult.mode === "translated") {
          setStatus(`Fetched ${originalArticles.length} articles and translated the edition to ${selectedLanguage}.`, false);
        } else if (translationResult.mode === "failed") {
          setStatus(`Fetched ${originalArticles.length} articles, but translation to ${selectedLanguage} failed.`, true);
        } else {
          setStatus(`Fetched ${originalArticles.length} articles across ${currentTopics.length} topic${currentTopics.length === 1 ? "" : "s"}.`, false);
        }
      } catch (error) {
        if (error.code === "ABORTED" || error.name === "AbortError") {
          restoreAfterAbort();
        } else if (error.code === "TIMEOUT") {
          originalArticles = snapshot.originalArticles;
          allArticles = snapshot.allArticles;
          currentTopics = snapshot.currentTopics;
          latestBriefing = snapshot.latestBriefing;
          latestEditionTimestamp = snapshot.latestEditionTimestamp;
          reasoningData = snapshot.reasoningData;
          if (allArticles.length) {
            renderHeroEditionCards(allArticles, currentTopics, {
              animate: false,
              createdAt: latestEditionTimestamp || new Date()
            });
            renderArticles(allArticles);
            renderTicker(allArticles);
            renderBriefing(latestBriefing, currentTopics);
            renderAgentLog(reasoningData);
            updateStatBar({ articles: originalArticles, topics: currentTopics });
            if (resultsContainer) resultsContainer.style.display = "block";
            loadVisuals();
          } else {
            renderDeferredState();
            renderHeroPreviewCards();
            renderTicker([]);
            renderBriefing("", []);
            renderAgentLog({});
            updateStatBar({ articles: [], topics: [] });
            clearVisualFrames();
            if (resultsContainer) resultsContainer.style.display = "none";
          }
          setStatus("The live edition is still compiling. Try a narrower topic mix or retry in a few seconds.", false);
        } else {
          originalArticles = snapshot.originalArticles;
          allArticles = snapshot.allArticles;
          currentTopics = snapshot.currentTopics;
          latestBriefing = snapshot.latestBriefing;
          latestEditionTimestamp = snapshot.latestEditionTimestamp;
          reasoningData = snapshot.reasoningData;
          if (allArticles.length) {
            renderHeroEditionCards(allArticles, currentTopics, {
              animate: false,
              createdAt: latestEditionTimestamp || new Date()
            });
          } else {
            renderHeroPreviewCards();
          }
          renderArticles(allArticles);
          renderTicker(allArticles);
          renderBriefing(latestBriefing, currentTopics);
          renderAgentLog(reasoningData);
          updateStatBar({ articles: originalArticles, topics: currentTopics });
          if (originalArticles.length) {
            if (resultsContainer) resultsContainer.style.display = "block";
            loadVisuals();
          } else {
            renderConnectionRetryState();
            clearVisualFrames();
            if (resultsContainer) resultsContainer.style.display = "none";
          }
          setStatus("Connection Refined - Please Retry", true);
        }
      } finally {
        if (!abortHandled) {
          setSynthesisProgress(false, languageSelect.value);
          setFetchLoading(false);
        }
        if (activeFetchController === requestController) activeFetchController = null;
        if (activeFetchReset === restoreAfterAbort) activeFetchReset = null;
      }
    }

    function toggleChatPanel(forceState) {
      chatPanelOpen = typeof forceState === "boolean" ? forceState : !chatPanelOpen;
      chatPanel.classList.toggle("is-open", chatPanelOpen);
      chatOverlay.classList.toggle("is-visible", chatPanelOpen);
      chatPanel.setAttribute("aria-hidden", chatPanelOpen ? "false" : "true");
      chatFab.setAttribute("aria-expanded", chatPanelOpen ? "true" : "false");
      if (chatPanelOpen) window.setTimeout(() => chatInput.focus(), 100);
    }

    function appendChatBubble(role, content, asHtml) {
      const bubble = document.createElement("div");
      bubble.className = `chat-bubble ${role}`;
      if (asHtml) bubble.innerHTML = content;
      else bubble.textContent = content;
      chatMessages.appendChild(bubble);
      chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function assistantMarkup(payload) {
      const response = escapeHtml(cleanText(payload && payload.response) || "No response returned.");
      const articles = Array.isArray(payload && payload.articles) ? payload.articles : [];
      const commentary = cleanText(payload && payload.sentiment_commentary);
      const cards = articles.length ? `
        <div class="chat-articles">
          ${articles.map((article) => `
            <div class="chat-article ${sentimentKey(article && article.sentiment)}">
              <p class="chat-article-title">
                <a href="${escapeHtml(safeUrl(article && article.link))}" target="_blank" rel="noopener noreferrer">${escapeHtml(headlineFor(article))}</a>
              </p>
              <div class="chat-article-meta">${escapeHtml(sourceFor(article))} · ${escapeHtml(publishedFor(article))}</div>
            </div>
          `).join("")}
        </div>
      ` : "";
      const commentaryBlock = commentary ? `<div class="chat-commentary">${escapeHtml(commentary)}</div>` : "";
      return `<p>${response}</p>${cards}${commentaryBlock}`;
    }

    function renderSuggestionChips(items) {
      const chips = (items && items.length ? items : DEFAULT_SUGGESTIONS).filter(Boolean).slice(0, 4);
      suggestionChips.innerHTML = chips.map((item) => `
        <button class="chat-chip" type="button" data-chip="${escapeHtml(item)}">${escapeHtml(item)}</button>
      `).join("");
    }

    async function sendChat(message) {
      const trimmed = cleanText(message);
      if (!trimmed) return;

      toggleChatPanel(true);
      appendChatBubble("user", trimmed, false);
      chatHistory.push({ role: "user", content: trimmed });
      chatInput.value = "";
      setChatLoading(true);

      try {
        const payload = await postJSON("/chat", {
          message: trimmed,
          history: chatHistory,
          last_topic: lastTopic,
          articles: originalArticles
        });

        lastTopic = payload.last_topic || lastTopic;
        chatHistory.push({ role: "assistant", content: cleanText(payload.response) });
        appendChatBubble("bot", assistantMarkup(payload), true);
        renderSuggestionChips(payload.suggestions || []);
      } catch (_error) {
        appendChatBubble("bot", "I ran into an issue while checking the latest coverage.", false);
      } finally {
        setChatLoading(false);
      }
    }

    heroFetchBtn.addEventListener("click", () => {
      if (topicInputs.some((input) => cleanText(input.value))) {
        fetchNews({ source: "hero" });
        return;
      }
      deskSection.scrollIntoView({ behavior: "smooth", block: "start" });
      window.setTimeout(() => topicInputs[0].focus(), 280);
    });

    heroInsightsBtn.addEventListener("click", () => {
      insightsBand.scrollIntoView({ behavior: "smooth", block: "start" });
    });

    if (heroBlankStack) {
      heroBlankStack.addEventListener("click", (event) => {
        const trigger = event.target.closest("#heroEditionArrow");
        if (!trigger) return;
        editionStage.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    }

    fetchBtn.addEventListener("click", () => fetchNews({ source: "desk" }));

    if (cancelRequestBtn) {
      cancelRequestBtn.addEventListener("click", () => cancelActiveRequest());
    }

    sampleBtn.addEventListener("click", () => {
      topicInputs[0].value = "Nvidia";
      topicInputs[1].value = "Cricket";
      topicInputs[2].value = "Climate Change";
      fetchNews({ source: "desk" });
    });

    languageSelect.addEventListener("change", async (event) => {
      const result = await translateArticles(event.target.value);
      if (Array.isArray(result.articles) && result.articles.length) {
        renderHeroEditionCards(result.articles, currentTopics, {
          animate: false,
          createdAt: latestEditionTimestamp || new Date()
        });
      }
      if (result.mode === "translated") {
        setStatus(`Showing the edition in ${event.target.value}.`, false);
      } else if (result.mode === "original") {
        setStatus("Showing original English headlines.", false);
      } else if (result.mode === "failed") {
        setStatus(`Translation to ${event.target.value} failed.`, true);
      }
    });

    agentLogToggle.addEventListener("click", () => toggleAgentLog());
    if (themeToggle) {
      themeToggle.addEventListener("click", () => {
        applyTheme(document.body.dataset.theme === "dark" ? "light" : "dark");
      });
    }
    chatFab.addEventListener("click", () => toggleChatPanel());
    chatCloseBtn.addEventListener("click", () => toggleChatPanel(false));
    chatOverlay.addEventListener("click", () => toggleChatPanel(false));
    chatSendBtn.addEventListener("click", () => sendChat(chatInput.value));

    chatInput.addEventListener("keydown", (event) => {
      if (event.key === "Enter") {
        event.preventDefault();
        sendChat(chatInput.value);
      }
    });

    quickBriefingBtn.addEventListener("click", () => sendChat("Give me a briefing"));

    suggestionChips.addEventListener("click", (event) => {
      const chip = event.target.closest("[data-chip]");
      if (!chip) return;
      sendChat(chip.getAttribute("data-chip") || "");
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && chatPanelOpen) toggleChatPanel(false);
    });

    renderHeroPreviewCards();
    renderQuietState();
    renderTicker([]);
    renderBriefing("", []);
    clearVisualFrames();
    renderAgentLog({});
    updateStatBar({ articles: [], topics: [] });
    renderSuggestionChips(DEFAULT_SUGGESTIONS);
    applyTheme(preferredTheme());
    window.requestAnimationFrame(() => {
      window.requestAnimationFrame(() => document.body.classList.add("is-ready"));
    });
    warmBackend();
  </script>
</body>
</html>
"""
