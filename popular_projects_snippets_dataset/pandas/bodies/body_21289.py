# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
nv.validate_any((), {"out": out, "keepdims": keepdims})
result = nanops.nanany(self._ndarray, axis=axis, skipna=skipna)
exit(self._wrap_reduction_result(axis, result))
