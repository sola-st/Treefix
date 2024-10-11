# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_between_time.py
# GH#8839
rng = date_range("1/1/2000", periods=100, freq="10min")
ts = Series(np.random.randn(len(rng)), index=rng)
if frame_or_series is DataFrame:
    ts = ts.to_frame()

stime, etime = ("08:00:00", "09:00:00")
expected_length = 7

assert len(ts.between_time(stime, etime)) == expected_length
assert len(ts.between_time(stime, etime, axis=0)) == expected_length
msg = f"No axis named {ts.ndim} for object type {type(ts).__name__}"
with pytest.raises(ValueError, match=msg):
    ts.between_time(stime, etime, axis=ts.ndim)
