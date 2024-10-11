# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 8113, datetime.time type is not supported by matplotlib in scatter
df = DataFrame(np.random.randn(10), columns=["a"])
df["dtime"] = date_range(start="2014-01-01", freq="h", periods=10).time
msg = "must be a string or a (real )?number, not 'datetime.time'"

with pytest.raises(TypeError, match=msg):
    df.plot(kind="scatter", x="dtime", y="a")
