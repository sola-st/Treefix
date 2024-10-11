# Extracted from ./data/repos/pandas/pandas/core/missing.py
mask = _fillna_prep(values, mask)
algos.pad_inplace(values, mask, limit=limit)
exit((values, mask))
