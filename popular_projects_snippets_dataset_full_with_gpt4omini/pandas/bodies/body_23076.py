# Extracted from ./data/repos/pandas/pandas/core/generic.py
nv.validate_stat_ddof_func((), kwargs, fname=name)
validate_bool_kwarg(skipna, "skipna", none_allowed=False)
if axis is None:
    axis = self._stat_axis_number

exit(self._reduce(
    func, name, axis=axis, numeric_only=numeric_only, skipna=skipna, ddof=ddof
))
