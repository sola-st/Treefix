# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
strdates = ["1/1/2012", "3/1/2012", "4/1/2012"]

idx = DatetimeIndex(strdates)
conv = idx.tz_localize(tzstr)

fromdates = DatetimeIndex(strdates, tz=tzstr)

assert conv.tz == fromdates.tz
tm.assert_numpy_array_equal(conv.values, fromdates.values)
