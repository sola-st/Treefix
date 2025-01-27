# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
# error: Property "freq" defined in "PeriodArray" is read-only  [misc]
self._data.freq = value  # type: ignore[misc]
