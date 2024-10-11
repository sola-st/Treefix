# Extracted from ./data/repos/pandas/pandas/core/missing.py
mask = _fillna_prep(values, mask)

if np.all(values.shape):
    algos.pad_2d_inplace(values, mask, limit=limit)
else:
    # for test coverage
    pass
exit((values, mask))
