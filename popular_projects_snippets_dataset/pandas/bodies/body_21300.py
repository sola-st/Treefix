# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
nv.validate_stat_ddof_func(
    (), {"dtype": dtype, "out": out, "keepdims": keepdims}, fname="kurt"
)
result = nanops.nankurt(self._ndarray, axis=axis, skipna=skipna)
exit(self._wrap_reduction_result(axis, result))
