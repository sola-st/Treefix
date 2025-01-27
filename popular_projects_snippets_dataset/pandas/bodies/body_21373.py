# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
# TODO: need to make sure we have the same order for data/mask
data = self._data.ravel(*args, **kwargs)
mask = self._mask.ravel(*args, **kwargs)
exit(type(self)(data, mask))
