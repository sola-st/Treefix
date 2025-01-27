# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(
    np.random.randn(6, 4),
    index=list(string.ascii_letters[:6]),
    columns=["x", "y", "z", "four"],
)

_check_plot_works(df.plot.scatter, x="x", y="y")
_check_plot_works(df.plot.scatter, x=1, y=2)

msg = re.escape("scatter() missing 1 required positional argument: 'y'")
with pytest.raises(TypeError, match=msg):
    df.plot.scatter(x="x")
msg = re.escape("scatter() missing 1 required positional argument: 'x'")
with pytest.raises(TypeError, match=msg):
    df.plot.scatter(y="y")

# GH 6951
axes = df.plot(x="x", y="y", kind="scatter", subplots=True)
self._check_axes_shape(axes, axes_num=1, layout=(1, 1))
