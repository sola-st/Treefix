# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_between_time.py
tz = timezones.maybe_get_tz(tzstr)

rng = date_range("4/16/2012", "5/1/2012", freq="H")
ts = Series(np.random.randn(len(rng)), index=rng)
if frame_or_series is DataFrame:
    ts = ts.to_frame()

ts_local = ts.tz_localize(tzstr)

t1, t2 = time(10, 0), time(11, 0)
result = ts_local.between_time(t1, t2)
expected = ts.between_time(t1, t2).tz_localize(tzstr)
tm.assert_equal(result, expected)
assert timezones.tz_compare(result.index.tz, tz)
