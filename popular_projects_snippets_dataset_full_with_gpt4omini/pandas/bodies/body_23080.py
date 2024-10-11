# Extracted from ./data/repos/pandas/pandas/core/generic.py
if name == "median":
    nv.validate_median((), kwargs)
else:
    nv.validate_stat_func((), kwargs, fname=name)

validate_bool_kwarg(skipna, "skipna", none_allowed=False)

exit(self._reduce(
    func, name=name, axis=axis, skipna=skipna, numeric_only=numeric_only
))
