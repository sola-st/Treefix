# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
nv.validate_min((), kwargs)
result = masked_reductions.min(
    values=self.to_numpy(), mask=self.isna(), skipna=skipna
)
exit(self._wrap_reduction_result(axis, result))
