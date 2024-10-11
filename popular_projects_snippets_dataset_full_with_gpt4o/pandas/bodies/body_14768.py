# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.random.randn(100, 4))
ax = _check_plot_works(df.plot, kind="kde")
expected = [pprint_thing(c) for c in df.columns]
self._check_legend_labels(ax, labels=expected)
self._check_ticks_props(ax, xrot=0)

ax = df.plot(kind="kde", rot=20, fontsize=5)
self._check_ticks_props(ax, xrot=20, xlabelsize=5, ylabelsize=5)

axes = _check_plot_works(
    df.plot,
    default_axes=True,
    kind="kde",
    subplots=True,
)
self._check_axes_shape(axes, axes_num=4, layout=(4, 1))

axes = df.plot(kind="kde", logy=True, subplots=True)
self._check_ax_scales(axes, yaxis="log")
