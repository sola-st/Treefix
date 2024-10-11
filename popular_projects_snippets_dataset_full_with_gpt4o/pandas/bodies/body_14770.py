# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
from matplotlib.patches import Rectangle

df = DataFrame(np.random.randn(100, 4))
series = df[0]

ax = _check_plot_works(df.plot.hist)
expected = [pprint_thing(c) for c in df.columns]
self._check_legend_labels(ax, labels=expected)

axes = _check_plot_works(
    df.plot.hist,
    default_axes=True,
    subplots=True,
    logy=True,
)
self._check_axes_shape(axes, axes_num=4, layout=(4, 1))
self._check_ax_scales(axes, yaxis="log")

axes = series.plot.hist(rot=40)
self._check_ticks_props(axes, xrot=40, yrot=0)
tm.close()

ax = series.plot.hist(cumulative=True, bins=4, density=True)
# height of last bin (index 5) must be 1.0
rects = [x for x in ax.get_children() if isinstance(x, Rectangle)]
tm.assert_almost_equal(rects[-1].get_height(), 1.0)
tm.close()

ax = series.plot.hist(cumulative=True, bins=4)
rects = [x for x in ax.get_children() if isinstance(x, Rectangle)]

tm.assert_almost_equal(rects[-2].get_height(), 100.0)
tm.close()

# if horizontal, yticklabels are rotated
axes = df.plot.hist(rot=50, fontsize=8, orientation="horizontal")
self._check_ticks_props(axes, xrot=0, yrot=50, ylabelsize=8)
