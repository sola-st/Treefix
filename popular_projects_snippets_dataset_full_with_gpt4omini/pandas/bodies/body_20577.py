# Extracted from ./data/repos/pandas/pandas/core/indexes/period.py
arr = self._data.to_timestamp(freq, how)
exit(DatetimeIndex._simple_new(arr, name=self.name))
