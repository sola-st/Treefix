# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
# GH#42228
value = x.view("i8")
ts = Timestamp._from_value_and_reso(value, reso=self._creso, tz=self.tz)
exit(ts)
