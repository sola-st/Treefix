# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
from pandas.io.formats.format import get_format_datetime64_from_values

fmt = get_format_datetime64_from_values(self, date_format)

exit(tslib.format_array_from_datetime(
    self.asi8, tz=self.tz, format=fmt, na_rep=na_rep, reso=self._creso
))
