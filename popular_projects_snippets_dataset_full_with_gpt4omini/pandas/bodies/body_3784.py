# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_between_time.py
# GH#8839
rng = date_range("1/1/2000", periods=100, freq="10min")
ts = DataFrame(np.random.randn(len(rng), len(rng)))
stime, etime = ("08:00:00", "09:00:00")
exp_len = 7

if axis in ["index", 0]:
    ts.index = rng
    assert len(ts.between_time(stime, etime)) == exp_len
    assert len(ts.between_time(stime, etime, axis=0)) == exp_len

if axis in ["columns", 1]:
    ts.columns = rng
    selected = ts.between_time(stime, etime, axis=1).columns
    assert len(selected) == exp_len
