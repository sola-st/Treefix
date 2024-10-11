# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
from pandas.tests.indexes.datetimes.test_timezones import fixed_off_no_name

off = fixed_off_no_name
start = datetime(2012, 3, 11, 5, 0, 0, tzinfo=off)
end = datetime(2012, 6, 11, 5, 0, 0, tzinfo=off)
rng = date_range(start=start, end=end)
assert off == rng.tz

idx = pd.Index([start, end])
assert off == idx.tz
