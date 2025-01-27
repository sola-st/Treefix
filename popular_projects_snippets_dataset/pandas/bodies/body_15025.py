# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
from matplotlib.patches import Rectangle

with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    _check_plot_works(hist_df.hist)

# make sure layout is handled
df = DataFrame(np.random.randn(100, 2))
df[2] = to_datetime(
    np.random.randint(
        812419200000000000,
        819331200000000000,
        size=100,
        dtype=np.int64,
    )
)
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(df.hist, grid=False)
self._check_axes_shape(axes, axes_num=3, layout=(2, 2))
assert not axes[1, 1].get_visible()

_check_plot_works(df[[2]].hist)
df = DataFrame(np.random.randn(100, 1))
_check_plot_works(df.hist)

# make sure layout is handled
df = DataFrame(np.random.randn(100, 5))
df[5] = to_datetime(
    np.random.randint(
        812419200000000000,
        819331200000000000,
        size=100,
        dtype=np.int64,
    )
)
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    axes = _check_plot_works(df.hist, layout=(4, 2))
self._check_axes_shape(axes, axes_num=6, layout=(4, 2))

# make sure sharex, sharey is handled
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    _check_plot_works(df.hist, sharex=True, sharey=True)

# handle figsize arg
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    _check_plot_works(df.hist, figsize=(8, 10))

# check bins argument
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    _check_plot_works(df.hist, bins=5)

# make sure xlabelsize and xrot are handled
ser = df[0]
xf, yf = 20, 18
xrot, yrot = 30, 40
axes = ser.hist(xlabelsize=xf, xrot=xrot, ylabelsize=yf, yrot=yrot)
self._check_ticks_props(
    axes, xlabelsize=xf, xrot=xrot, ylabelsize=yf, yrot=yrot
)

xf, yf = 20, 18
xrot, yrot = 30, 40
axes = df.hist(xlabelsize=xf, xrot=xrot, ylabelsize=yf, yrot=yrot)
self._check_ticks_props(
    axes, xlabelsize=xf, xrot=xrot, ylabelsize=yf, yrot=yrot
)

tm.close()

ax = ser.hist(cumulative=True, bins=4, density=True)
# height of last bin (index 5) must be 1.0
rects = [x for x in ax.get_children() if isinstance(x, Rectangle)]
tm.assert_almost_equal(rects[-1].get_height(), 1.0)

tm.close()
ax = ser.hist(log=True)
# scale of y must be 'log'
self._check_ax_scales(ax, yaxis="log")

tm.close()

# propagate attr exception from matplotlib.Axes.hist
with tm.external_error_raised(AttributeError):
    ser.hist(foo="bar")
