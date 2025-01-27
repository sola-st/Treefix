# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = hist_df
numeric_cols = df._get_numeric_data().columns
labels = [pprint_thing(c) for c in numeric_cols]

# if horizontal, yticklabels are rotated
ax = df.plot.box(rot=50, fontsize=8, vert=False)
self._check_ticks_props(ax, xrot=0, yrot=50, ylabelsize=8)
self._check_text_labels(ax.get_yticklabels(), labels)
assert len(ax.lines) == 7 * len(numeric_cols)

axes = _check_plot_works(
    df.plot.box,
    default_axes=True,
    subplots=True,
    vert=False,
    logx=True,
)
self._check_axes_shape(axes, axes_num=3, layout=(1, 3))
self._check_ax_scales(axes, xaxis="log")
for ax, label in zip(axes, labels):
    self._check_text_labels(ax.get_yticklabels(), [label])
    assert len(ax.lines) == 7

positions = np.array([3, 2, 8])
ax = df.plot.box(positions=positions, vert=False)
self._check_text_labels(ax.get_yticklabels(), labels)
tm.assert_numpy_array_equal(ax.yaxis.get_ticklocs(), positions)
assert len(ax.lines) == 7 * len(numeric_cols)
