# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_between_time.py
# issue 8839
rng = date_range("1/1/2000", periods=100, freq="10min")
mask = np.arange(0, len(rng))
rand_data = np.random.randn(len(rng), len(rng))
ts = DataFrame(rand_data, index=rng, columns=rng)
stime, etime = ("08:00:00", "09:00:00")

msg = "Index must be DatetimeIndex"
if axis in ["columns", 1]:
    ts.index = mask
    with pytest.raises(TypeError, match=msg):
        ts.between_time(stime, etime)
    with pytest.raises(TypeError, match=msg):
        ts.between_time(stime, etime, axis=0)

if axis in ["index", 0]:
    ts.columns = mask
    with pytest.raises(TypeError, match=msg):
        ts.between_time(stime, etime, axis=1)
