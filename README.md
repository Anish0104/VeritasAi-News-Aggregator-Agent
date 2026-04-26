# VeritasAI News Aggregator Agent

VeritasAI is a live news aggregation and synthesis project that combines a custom editorial-style frontend with a Colab-friendly notebook workflow.

This repo currently includes the core files needed for the latest UI and notebook flow:

- `templates.py`: the full frontend template, including the hero card system, insights section, theme handling, and client-side interactions.
- `generate_veritas_notebook.py`: generates the Google Colab submission notebook from the current local source files.
- `VeritasAI_Colab_Submission.ipynb`: the generated Colab notebook artifact ready to open in Google Colab.

## Highlights

- Live edition workflow for up to three news topics
- Editorial hero card deck with interactive hover and focus states
- Light and dark mode support
- Insights area with a word cloud and Plotly-based charts
- Chat assistant and reasoning log UI built into the template

## Recommended Workflow

1. Update `templates.py` locally.
2. Regenerate the notebook with:

```bash
python3 generate_veritas_notebook.py
```

3. Open `VeritasAI_Colab_Submission.ipynb` in Colab when you are ready to run or share the project.

## Notes

- The notebook file is generated from the current local sources, so it should be refreshed after UI or notebook-generator changes.
- This repo intentionally keeps the committed scope small and focused on the current deliverables.
