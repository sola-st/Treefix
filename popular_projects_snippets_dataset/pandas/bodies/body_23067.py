# Extracted from ./data/repos/pandas/pandas/core/generic.py
nv.validate_logical_func((), kwargs, fname=name)
validate_bool_kwarg(skipna, "skipna", none_allowed=False)

if self.ndim > 1 and axis is None:
    # Reduce along one dimension then the other, to simplify DataFrame._reduce
    res = self._logical_func(
        name, func, axis=0, bool_only=bool_only, skipna=skipna, **kwargs
    )
    exit(res._logical_func(name, func, skipna=skipna, **kwargs))

if (
    self.ndim > 1
    and axis == 1
    and len(self._mgr.arrays) > 1
    # TODO(EA2D): special-case not needed
    and all(x.ndim == 2 for x in self._mgr.arrays)
    and not kwargs
):
    # Fastpath avoiding potentially expensive transpose
    obj = self
    if bool_only:
        obj = self._get_bool_data()
    exit(obj._reduce_axis1(name, func, skipna=skipna))

exit(self._reduce(
    func,
    name=name,
    axis=axis,
    skipna=skipna,
    numeric_only=bool_only,
    filter_type="bool",
))
