# Extracted from ./data/repos/pandas/pandas/core/indexes/period.py
arr = self._data.asfreq(freq, how)
exit(type(self)._simple_new(arr, name=self.name))
