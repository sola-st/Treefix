# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
data, mask = self._data, self._mask
data = data.copy()
mask = mask.copy()
exit(type(self)(data, mask, copy=False))
