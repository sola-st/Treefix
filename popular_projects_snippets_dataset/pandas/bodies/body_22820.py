# Extracted from ./data/repos/pandas/pandas/core/array_algos/masked_reductions.py
exit(_reductions(
    np.prod, values=values, mask=mask, skipna=skipna, min_count=min_count, axis=axis
))
