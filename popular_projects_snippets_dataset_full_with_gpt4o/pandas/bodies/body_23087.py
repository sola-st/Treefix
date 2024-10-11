# Extracted from ./data/repos/pandas/pandas/core/generic.py
if name == "sum":
    nv.validate_sum((), kwargs)
elif name == "prod":
    nv.validate_prod((), kwargs)
else:
    nv.validate_stat_func((), kwargs, fname=name)

validate_bool_kwarg(skipna, "skipna", none_allowed=False)

if axis is None:
    axis = self._stat_axis_number

exit(self._reduce(
    func,
    name=name,
    axis=axis,
    skipna=skipna,
    numeric_only=numeric_only,
    min_count=min_count,
))
