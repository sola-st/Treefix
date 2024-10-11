# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
if self.ndim > 1:
    exit([x.tolist() for x in self])
dtype = None if self._hasna else self._data.dtype
exit(self.to_numpy(dtype=dtype).tolist())
