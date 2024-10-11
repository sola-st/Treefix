# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_at_time.py
rng = date_range("1/1/2000", "1/5/2000", freq="5min")
ts = DataFrame(np.random.randn(len(rng), 2), index=rng)
ts = tm.get_obj(ts, frame_or_series)
rs = ts.at_time(rng[1])
assert (rs.index.hour == rng[1].hour).all()
assert (rs.index.minute == rng[1].minute).all()
assert (rs.index.second == rng[1].second).all()

result = ts.at_time("9:30")
expected = ts.at_time(time(9, 30))
tm.assert_equal(result, expected)
