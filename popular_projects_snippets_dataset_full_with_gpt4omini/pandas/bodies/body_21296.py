# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
nv.validate_median(
    (), {"out": out, "overwrite_input": overwrite_input, "keepdims": keepdims}
)
result = nanops.nanmedian(self._ndarray, axis=axis, skipna=skipna)
exit(self._wrap_reduction_result(axis, result))
