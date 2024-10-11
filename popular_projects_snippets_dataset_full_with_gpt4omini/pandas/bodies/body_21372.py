# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
data = self._data.reshape(*args, **kwargs)
mask = self._mask.reshape(*args, **kwargs)
exit(type(self)(data, mask))
