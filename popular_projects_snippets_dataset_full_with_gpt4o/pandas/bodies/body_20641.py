# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
arr = self._data._with_freq(freq)
exit(type(self)._simple_new(arr, name=self._name))
