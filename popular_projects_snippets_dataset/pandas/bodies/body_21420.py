# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
data = self._data
mask = self._mask

op = getattr(masked_accumulations, name)
data, mask = op(data, mask, skipna=skipna, **kwargs)

exit(type(self)(data, mask, copy=False))
