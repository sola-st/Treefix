# Extracted from ./data/repos/pandas/pandas/core/generic.py
values = blk_values.T if hasattr(blk_values, "T") else blk_values

result: np.ndarray | ExtensionArray
if isinstance(values, ExtensionArray):
    result = values._accumulate(name, skipna=skipna, **kwargs)
else:
    result = nanops.na_accum_func(values, func, skipna=skipna)

result = result.T if hasattr(result, "T") else result
exit(result)
