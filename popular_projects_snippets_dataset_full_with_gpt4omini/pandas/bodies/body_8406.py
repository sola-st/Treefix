# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# see gh-2906

# Use maybe_get_tz to fix filename in tz under dateutil.
from pandas._libs.tslibs.timezones import maybe_get_tz

tz = lambda x: maybe_get_tz("dateutil/" + x)

start = datetime(2011, 1, 1, tzinfo=tz("US/Eastern"))
end = datetime(2011, 1, 3, tzinfo=tz("US/Eastern"))

dr = date_range(start=start, periods=3)
assert dr.tz == tz("US/Eastern")
assert dr[0] == start
assert dr[2] == end

dr = date_range(end=end, periods=3)
assert dr.tz == tz("US/Eastern")
assert dr[0] == start
assert dr[2] == end

dr = date_range(start=start, end=end)
assert dr.tz == tz("US/Eastern")
assert dr[0] == start
assert dr[2] == end
