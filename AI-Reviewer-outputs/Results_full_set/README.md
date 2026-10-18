# Results_full_set

AI Reviewer (GRAIL) outputs for the 18-proposal generalization batch: 18 proposals x 5 systems = 90 papers
(inputs: `AI-Scientist-generated-papers/needs_ai_reviewing_set/`).

| File | Description |
|---|---|
| `results.jsonl` | Raw reviewer export, one record per paper: three individual model reviews, failures, and the synthesis review |
| `results_scores.csv` | Flat per-paper score matrix (same schema as `../Results_pilot_set/results_scores.csv`) derived from `results.jsonl` |

All 90 reviews completed with all three reviewer models and a synthesis score. Paper identity is encoded in the
`filename` field of each record (`FAxxxx_<System>.pdf`); `paper_id` and `source` in the CSV are parsed from it.
