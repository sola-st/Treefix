# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
nv.validate_stat_ddof_func(
    (), {"dtype": dtype, "out": out, "keepdims": keepdims}, fname="sem"
)
result = nanops.nansem(self._ndarray, axis=axis, skipna=skipna, ddof=ddof)
exit(self._wrap_reduction_result(axis, result))
