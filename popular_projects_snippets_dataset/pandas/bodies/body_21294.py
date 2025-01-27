# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
nv.validate_prod((), kwargs)
result = nanops.nanprod(
    self._ndarray, axis=axis, skipna=skipna, min_count=min_count
)
exit(self._wrap_reduction_result(axis, result))
