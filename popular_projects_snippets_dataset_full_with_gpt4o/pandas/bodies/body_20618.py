# Extracted from ./data/repos/pandas/pandas/core/indexes/extension.py
assert result.dtype == self._data._ndarray.dtype
exit(self._data._from_backing_data(result))
