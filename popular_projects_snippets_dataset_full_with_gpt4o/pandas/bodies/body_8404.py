# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# see gh-2906
tz = timezone("US/Eastern")
start = tz.localize(datetime(2011, 1, 1))
end = tz.localize(datetime(2011, 1, 3))

dr = date_range(start=start, periods=3)
assert dr.tz.zone == tz.zone
assert dr[0] == start
assert dr[2] == end

dr = date_range(end=end, periods=3)
assert dr.tz.zone == tz.zone
assert dr[0] == start
assert dr[2] == end

dr = date_range(start=start, end=end)
assert dr.tz.zone == tz.zone
assert dr[0] == start
assert dr[2] == end
