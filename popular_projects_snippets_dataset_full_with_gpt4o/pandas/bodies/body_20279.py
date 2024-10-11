# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
arr = self._data.strftime(date_format)
exit(Index(arr, name=self.name, dtype=object))
