# Reviewer configuration

The AI Reviewer is the GRAIL hosted multi-model review service. Each paper is reviewed independently by three models,
and a synthesis layer aggregates their reviews. Scores: Quality, Clarity, Significance, Originality and Confidence per
reviewer, 1-4 for dimensions, plus an Overall score; the synthesis review carries the same fields.

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

## Prompts and decoding settings

