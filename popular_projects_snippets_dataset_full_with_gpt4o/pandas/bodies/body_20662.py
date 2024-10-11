# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
result = super().insert(loc, item)
if isinstance(result, type(self)):
    # i.e. parent class method did not cast
    result._data._freq = self._get_insert_freq(loc, item)
exit(result)
