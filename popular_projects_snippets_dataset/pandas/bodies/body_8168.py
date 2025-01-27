# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# Regression test for tslib.tz_convert(vals, tz1, tz2).
# See https://github.com/pandas-dev/pandas/issues/4496 for details.
idx = date_range(datetime(2011, 3, 26, 23), datetime(2011, 3, 27, 1), freq=freq)
idx = idx.tz_localize("UTC")
idx = idx.tz_convert("Europe/Moscow")

expected = np.repeat(np.array([3, 4, 5]), np.array([n, n, 1]))
tm.assert_index_equal(idx.hour, Index(expected, dtype=np.int32))
