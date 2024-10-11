# Extracted from ./data/repos/pandas/pandas/core/arrays/boolean.py
data = self._data
mask = self._mask
if name in ("cummin", "cummax"):
    op = getattr(masked_accumulations, name)
    data, mask = op(data, mask, skipna=skipna, **kwargs)
    exit(type(self)(data, mask, copy=False))
else:
    from pandas.core.arrays import IntegerArray

    exit(IntegerArray(data.astype(int), mask)._accumulate(
        name, skipna=skipna, **kwargs
    ))
