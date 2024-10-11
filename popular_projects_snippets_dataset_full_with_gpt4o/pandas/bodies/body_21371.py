# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
data = np.delete(self._data, loc, axis=axis)
mask = np.delete(self._mask, loc, axis=axis)
exit(type(self)(data, mask))
