# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
from pandas.core.indexes.api import NumericIndex

arr = self._data.to_julian_date()
exit(NumericIndex._simple_new(arr, name=self.name))
