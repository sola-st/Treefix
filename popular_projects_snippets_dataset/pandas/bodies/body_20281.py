# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
arr = self._data.tz_localize(tz, ambiguous, nonexistent)
exit(type(self)._simple_new(arr, name=self.name))
