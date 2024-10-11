# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
nv.validate_all((), {"out": out, "keepdims": keepdims})
result = nanops.nanall(self._ndarray, axis=axis, skipna=skipna)
exit(self._wrap_reduction_result(axis, result))
