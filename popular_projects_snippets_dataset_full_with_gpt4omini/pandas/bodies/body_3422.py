# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_at_time.py
tz = timezones.maybe_get_tz(tzstr)

rng = date_range("4/16/2012", "5/1/2012", freq="H")
ts = frame_or_series(np.random.randn(len(rng)), index=rng)

ts_local = ts.tz_localize(tzstr)

result = ts_local.at_time(time(10, 0))
expected = ts.at_time(time(10, 0)).tz_localize(tzstr)
tm.assert_equal(result, expected)
assert timezones.tz_compare(result.index.tz, tz)
