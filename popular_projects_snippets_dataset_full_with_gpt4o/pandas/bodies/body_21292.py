# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
nv.validate_max((), kwargs)
result = nanops.nanmax(
    values=self._ndarray, axis=axis, mask=self.isna(), skipna=skipna
)
exit(self._wrap_reduction_result(axis, result))
