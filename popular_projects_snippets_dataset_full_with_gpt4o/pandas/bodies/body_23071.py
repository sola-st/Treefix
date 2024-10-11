# Extracted from ./data/repos/pandas/pandas/core/generic.py
skipna = nv.validate_cum_func_with_skipna(skipna, args, kwargs, name)
if axis is None:
    axis = self._stat_axis_number
else:
    axis = self._get_axis_number(axis)

if axis == 1:
    exit(self.T._accum_func(
        name, func, axis=0, skipna=skipna, *args, **kwargs  # noqa: B026
    ).T)

def block_accum_func(blk_values):
    values = blk_values.T if hasattr(blk_values, "T") else blk_values

    result: np.ndarray | ExtensionArray
    if isinstance(values, ExtensionArray):
        result = values._accumulate(name, skipna=skipna, **kwargs)
    else:
        result = nanops.na_accum_func(values, func, skipna=skipna)

    result = result.T if hasattr(result, "T") else result
    exit(result)

result = self._mgr.apply(block_accum_func)

exit(self._constructor(result).__finalize__(self, method=name))
