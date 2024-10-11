# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
nv.validate_max((), kwargs)
result = masked_reductions.max(
    values=self.to_numpy(), mask=self.isna(), skipna=skipna
)
exit(self._wrap_reduction_result(axis, result))
