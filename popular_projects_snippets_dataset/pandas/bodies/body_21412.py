# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
nv.validate_prod((), kwargs)
result = masked_reductions.prod(
    self._data,
    self._mask,
    skipna=skipna,
    min_count=min_count,
    axis=axis,
)
exit(self._wrap_reduction_result(
    "prod", result, skipna=skipna, axis=axis, **kwargs
))
