# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
nv.validate_sum((), kwargs)
result = nanops.nansum(
    self._ndarray, axis=axis, skipna=skipna, min_count=min_count
)
exit(self._wrap_reduction_result(axis, result))
