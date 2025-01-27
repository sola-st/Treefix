# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
nv.validate_mean((), kwargs)
result = masked_reductions.mean(
    self._data,
    self._mask,
    skipna=skipna,
    axis=axis,
)
exit(self._wrap_reduction_result(
    "mean", result, skipna=skipna, axis=axis, **kwargs
))
