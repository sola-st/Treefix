# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
from pandas._libs.tslibs.timezones import dateutil_gettz as gettz

rng = date_range("20090415", "20090519", tz=gettz("US/Eastern"))
stamp = rng[0]

ts = Timestamp("20090415", tz=gettz("US/Eastern"))
assert ts == stamp
