# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_at_time.py
# time doesn't exist
rng = date_range("1/1/2012", freq="23Min", periods=384)
ts = DataFrame(np.random.randn(len(rng)), rng)
ts = tm.get_obj(ts, frame_or_series)
rs = ts.at_time("16:00")
assert len(rs) == 0
