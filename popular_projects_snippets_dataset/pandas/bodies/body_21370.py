# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
data = self._data.swapaxes(axis1, axis2)
mask = self._mask.swapaxes(axis1, axis2)
exit(type(self)(data, mask))
