# Reviewer configuration

The AI Reviewer is the GRAIL hosted multi-model review service. Each paper is reviewed independently by three models
(GPT-5.4, Gemini 3.1 Pro, Claude Opus 4.6), using the same prompts for all three. Each model reviews in two passes
(an initial review, then a self-calibration pass), and GPT-5.4 then writes a synthesis review that aggregates the three.
Scores: Quality, Clarity, Significance and Originality on a 1-4 scale; Overall on a 1-6 scale; Confidence on a 1-5 scale.
The prompts were identical for the pilot set (reviewed 2026-04-15) and the generalization batch (reviewed 2026-07-15 to 2026-07-16).

| File | Contents |
|---|---|
| `prompts/A_scoring_rubric.md` | Scoring rubric, included in every review and synthesis call |
| `prompts/B_pass1_initial_review.md` | Pass 1 prompt (initial review) |
| `prompts/C_pass2_self_calibration.md` | Pass 2 prompt (self-calibration) |
| `prompts/D_synthesis.md` | Synthesis prompt |
| `decoding_settings.md` | Per-model decoding settings, score ranges and model versions |

The JSON output schema that the prompts refer to is reflected in the field names of `results.jsonl`.

## Reviewer models (as recorded in the exports)

| Display name | Model string |
|---|---|
| GPT 5.4 | `azure/gpt-5.4-review` |
| Gemini 3.1 Pro | `gemini/gemini-3.1-pro-preview` |
| Claude Opus 4.6 | `anthropic/claude-opus-4-6` |

## Review dates (from export timestamps)

| Set | Records | First submitted | Last completed |
|---|---:|---|---|
| Pilot (`Results_pilot_set`) | 75 | 2026-04-15 | 2026-04-15 |
| Generalization batch (`Results_full_set`) | 90 | 2026-07-15 | 2026-07-16 |
