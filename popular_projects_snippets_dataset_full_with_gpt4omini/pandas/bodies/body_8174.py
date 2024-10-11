# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH#46460
times = ["2015-03-08 01:00", "2015-03-08 02:00", "2015-03-08 03:00"]
index = DatetimeIndex(times)

res = index.tz_localize(utc_fixture)
assert not tm.shares_memory(res, index)

res2 = index._data.tz_localize(utc_fixture)
assert not tm.shares_memory(index._data, res2)
