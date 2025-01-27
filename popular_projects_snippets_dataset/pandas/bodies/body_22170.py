# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
if nullable:
    if mask.ndim == 2:
        mask = mask[:, 0]
    exit(FloatingArray(np.sqrt(vals), mask.view(np.bool_)))
exit(np.sqrt(vals))
