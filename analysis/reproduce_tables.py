# Reproduces the accounting table and the generalization table (FARS vs Sakana v1) in the paper.
# Run from the repository root:  python analysis/reproduce_tables.py
# Needs: pandas, numpy, scipy.  Reads the two results_scores.csv files and the manifest of the generalization batch.
import re
import numpy as np, pandas as pd
from scipy.stats import wilcoxon

PILOT = "AI-Reviewer-outputs/Results_pilot_set/results_scores.csv"
NEW   = "AI-Reviewer-outputs/Results_full_set/results_scores.csv"
MAN   = "AI-Scientist-generated-papers/needs_ai_reviewing_set/manifest.csv"
SCORE, REF = "synthesis_overall", "sakanav1"
ORDER = [("Sakana v1", "sakanav1"), ("Sakana v2", "sakanav2"), ("CycleResearcher", "cycleresearcher"),
         ("Data-to-Paper", "datatopaper"), ("FARS", "fars")]
norm = lambda s: re.sub(r"[^a-z0-9]", "", str(s).lower())

pilot, new, man = pd.read_csv(PILOT), pd.read_csv(NEW), pd.read_csv(MAN)
for d, c in ((pilot, "source"), (new, "source"), (man, "system")): d["k"] = d[c].map(norm)

print("=== Accounting (generated / scored per system) ===")
print(f"{'System':16s} pilot_gen pilot_scored new_gen new_scored total_gen")
for lab, k in ORDER:
    pg = pilot[pilot.k == k].paper_id.nunique(); ps = int(pilot[pilot.k == k][SCORE].notna().sum())
    ng = man[man.k == k].proposal_id.nunique();  ns = int(new[new.k == k][SCORE].notna().sum())
    print(f"{lab:16s} {pg:9d} {ps:12d} {ng:7d} {ns:10d} {pg + ng:9d}")

def bh(p):
    p = np.asarray(p, float); n = len(p); o = np.argsort(p); q = np.empty(n); prev = 1.0
    for rank, i in zip(range(n, 0, -1), o[::-1]):
        prev = min(prev, p[i] * n / rank); q[i] = prev
    return q

def table(df, label):
    w = df.pivot_table(index="paper_id", columns="k", values=SCORE)
    print(f"\n=== {label}: {len(w)} proposals; mean +/- SD (ddof=1); exact paired Wilcoxon vs Sakana v1; BH across 4 comparisons ===")
    for lab, k in ORDER:
        x = w[k].dropna(); print(f"  {lab:16s} n={len(x):3d}  {x.mean():.2f} +/- {x.std(ddof=1):.2f}")
    ks = [k for _, k in ORDER if k != REF]; ps = []
    for k in ks:
        d = (w[k] - w[REF]).dropna()
        if (d == 0).all(): ps.append(np.nan); continue          # identical scores on every proposal: no test defined (n/a)
        try: ps.append(wilcoxon(d, method="exact").pvalue)
        except ValueError: ps.append(np.nan)
    qs = bh(np.nan_to_num(ps, nan=1.0))
    for (lab, k), p, q in zip([o for o in ORDER if o[1] != REF], ps, qs):
        ptxt = "n/a (all differences zero)" if np.isnan(p) else ("<0.0001" if p < 1e-4 else f"{p:.4f}")
        print(f"  vs Sakana v1: {lab:16s} p={ptxt:>8s}  q(BH)={'n/a' if np.isnan(p) else format(q, '.4f')}")

table(pilot, "Pilot (15 proposals)"); table(new, "Generalization batch (18 proposals)"); table(pd.concat([pilot, new]), "Combined (33 proposals)")
