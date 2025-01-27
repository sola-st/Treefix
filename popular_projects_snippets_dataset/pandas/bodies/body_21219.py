# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
nv.validate_sum(
    (), {"dtype": dtype, "out": out, "keepdims": keepdims, "initial": initial}
)

result = nanops.nansum(
    self._ndarray, axis=axis, skipna=skipna, min_count=min_count
)
exit(self._wrap_reduction_result(axis, result))
