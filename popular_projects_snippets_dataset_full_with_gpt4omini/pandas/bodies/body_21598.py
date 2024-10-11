# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
npvalue = self._validate_setitem_value(value).view("M8[ns]")

# Cast to M8 to get datetime-like NaT placement,
#  similar to dtl._period_dispatch
m8arr = self._ndarray.view("M8[ns]")
exit(m8arr.searchsorted(npvalue, side=side, sorter=sorter))
