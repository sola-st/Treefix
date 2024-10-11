# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
result = super().delete(loc)
result._data._freq = self._get_delete_freq(loc)
exit(result)
