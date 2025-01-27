# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
from pandas.core.indexes.api import PeriodIndex

arr = self._data.to_period(freq)
exit(PeriodIndex._simple_new(arr, name=self.name))
