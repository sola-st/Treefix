# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
# view e.g. i8 back to M8[ns]
result = result.view(self._data._ndarray.dtype)
exit(self._data._from_backing_data(result))
