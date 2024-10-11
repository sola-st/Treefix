# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
nv.validate_stat_ddof_func((), kwargs, fname="var")
result = masked_reductions.var(
    self._data,
    self._mask,
    skipna=skipna,
    axis=axis,
    ddof=ddof,
)
exit(self._wrap_reduction_result(
    "var", result, skipna=skipna, axis=axis, **kwargs
))
