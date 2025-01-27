# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
from pandas._libs.tslibs.timezones import dateutil_gettz

tz = dateutil_gettz("US/Eastern")

early_start = datetime(2011, 1, 1)
early_end = datetime(2011, 3, 1)

late_start = datetime(2011, 3, 1)
late_end = datetime(2011, 5, 1)

early_dr = date_range(start=early_start, end=early_end, tz=tz, freq=MonthEnd())
late_dr = date_range(start=late_start, end=late_end, tz=tz, freq=MonthEnd())

early_dr.union(late_dr, sort=sort)
