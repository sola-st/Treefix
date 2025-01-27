# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
from pandas.io.formats.format import get_format_datetime64

formatter = get_format_datetime64(is_dates_only_=self._is_dates_only)
exit(lambda x: f"'{formatter(x)}'")
