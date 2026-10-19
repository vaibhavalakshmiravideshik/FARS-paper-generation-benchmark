# Decoding settings

Settings as configured in the AI Reviewer service, as reported by the service operator for the generalization-batch run (2026-07-15 to 2026-07-16).
The pilot set was reviewed on 2026-04-15 with the same prompts; its decoding settings were not separately recorded.
Each reviewer model reviews a paper in two passes (Pass 1: initial review; Pass 2: self-calibration), using the
same prompts for all three models. GPT-5.4 then writes the synthesis review.

| Model | Settings |
|---|---|
| GPT-5.4 (reviews and synthesis) | Reasoning effort "high". Temperature, top-p and max tokens were not sent: with reasoning enabled, GPT-5.4 does not accept temperature or top-p, so its fixed defaults apply (temperature 1; top-p not published by OpenAI). Max output tokens left at the model limit (128,000, including reasoning tokens). |
| Gemini 3.1 Pro | Temperature 0.4 in Pass 1 and 0.3 in Pass 2. Defaults otherwise: top-p 0.95, top-k 64, max output tokens 65,536 (model limit), thinking level "high". |
| Claude Opus 4.6 | Temperature 1, adaptive thinking, effort "medium", max tokens 16,000. Top-p and top-k were not set. |

## Score ranges

Dimension scores (Quality, Clarity, Significance, Originality): 1-4. Overall score: 1-6. Confidence: 1-5.
The synthesis review uses the same ranges.

## Model versions

| Display name | Version |
|---|---|
| GPT-5.4 | `gpt-5.4-review` (Azure deployment name for gpt-5.4, version 2026-03-05) |
| Gemini 3.1 Pro | `gemini-3.1-pro-preview` |
| Claude Opus 4.6 | `claude-opus-4-6` |
