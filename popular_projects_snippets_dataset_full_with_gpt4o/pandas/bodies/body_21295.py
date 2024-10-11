# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
nv.validate_mean((), {"dtype": dtype, "out": out, "keepdims": keepdims})
result = nanops.nanmean(self._ndarray, axis=axis, skipna=skipna)
exit(self._wrap_reduction_result(axis, result))
