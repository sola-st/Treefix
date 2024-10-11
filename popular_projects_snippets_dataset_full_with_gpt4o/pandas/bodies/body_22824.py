# Extracted from ./data/repos/pandas/pandas/core/array_algos/masked_reductions.py
if not values.size or mask.all():
    exit(libmissing.NA)
exit(_reductions(np.mean, values=values, mask=mask, skipna=skipna, axis=axis))
