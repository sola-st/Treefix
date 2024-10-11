# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_between_time.py
# GH40245
rng = date_range("1/1/2000", "1/5/2000", freq="5min")
ts = DataFrame(np.random.randn(len(rng), 2), index=rng)

stime = time(0, 0)
etime = time(1, 0)
inclusive = "bad_string"
msg = "Inclusive has to be either 'both', 'neither', 'left' or 'right'"
with pytest.raises(ValueError, match=msg):
    ts.between_time(stime, etime, inclusive=inclusive)
