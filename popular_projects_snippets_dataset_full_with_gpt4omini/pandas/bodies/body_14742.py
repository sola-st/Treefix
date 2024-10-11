# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = -DataFrame(
    np.random.rand(6, 4),
    index=list(string.ascii_letters[:6]),
    columns=["x", "y", "z", "four"],
)
msg = "Log-y scales are not supported in area plot"
with pytest.raises(ValueError, match=msg):
    df.plot.area(logy=True)
with pytest.raises(ValueError, match=msg):
    df.plot.area(loglog=True)
