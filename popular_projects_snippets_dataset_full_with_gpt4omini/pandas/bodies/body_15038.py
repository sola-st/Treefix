# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
from matplotlib.patches import Rectangle

from pandas.plotting._matplotlib.hist import _grouped_hist

df = DataFrame(np.random.randn(500, 1), columns=["A"])
df["B"] = to_datetime(
    np.random.randint(
        812419200000000000,
        819331200000000000,
        size=500,
        dtype=np.int64,
    )
)
df["C"] = np.random.randint(0, 4, 500)
df["D"] = ["X"] * 500

axes = _grouped_hist(df.A, by=df.C)
self._check_axes_shape(axes, axes_num=4, layout=(2, 2))

tm.close()
axes = df.hist(by=df.C)
self._check_axes_shape(axes, axes_num=4, layout=(2, 2))

tm.close()
# group by a key with single value
axes = df.hist(by="D", rot=30)
self._check_axes_shape(axes, axes_num=1, layout=(1, 1))
self._check_ticks_props(axes, xrot=30)

tm.close()
# make sure kwargs to hist are handled
xf, yf = 20, 18
xrot, yrot = 30, 40

axes = _grouped_hist(
    df.A,
    by=df.C,
    cumulative=True,
    bins=4,
    xlabelsize=xf,
    xrot=xrot,
    ylabelsize=yf,
    yrot=yrot,
    density=True,
)
# height of last bin (index 5) must be 1.0
for ax in axes.ravel():
    rects = [x for x in ax.get_children() if isinstance(x, Rectangle)]
    height = rects[-1].get_height()
    tm.assert_almost_equal(height, 1.0)
self._check_ticks_props(
    axes, xlabelsize=xf, xrot=xrot, ylabelsize=yf, yrot=yrot
)

tm.close()
axes = _grouped_hist(df.A, by=df.C, log=True)
# scale of y must be 'log'
self._check_ax_scales(axes, yaxis="log")

tm.close()
# propagate attr exception from matplotlib.Axes.hist
with tm.external_error_raised(AttributeError):
    _grouped_hist(df.A, by=df.C, foo="bar")

msg = "Specify figure size by tuple instead"
with pytest.raises(ValueError, match=msg):
    df.hist(by="C", figsize="default")
