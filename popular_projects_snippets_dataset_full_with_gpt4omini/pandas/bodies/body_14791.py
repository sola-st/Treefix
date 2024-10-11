# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(
    np.random.rand(5, 3),
    columns=["X", "Y", "Z"],
    index=["a", "b", "c", "d", "e"],
)
msg = "pie requires either y column or 'subplots=True'"
with pytest.raises(ValueError, match=msg):
    df.plot.pie()

ax = _check_plot_works(df.plot.pie, y="Y")
self._check_text_labels(ax.texts, df.index)

ax = _check_plot_works(df.plot.pie, y=2)
self._check_text_labels(ax.texts, df.index)

axes = _check_plot_works(
    df.plot.pie,
    default_axes=True,
    subplots=True,
)
assert len(axes) == len(df.columns)
for ax in axes:
    self._check_text_labels(ax.texts, df.index)
for ax, ylabel in zip(axes, df.columns):
    assert ax.get_ylabel() == ylabel

labels = ["A", "B", "C", "D", "E"]
color_args = ["r", "g", "b", "c", "m"]
axes = _check_plot_works(
    df.plot.pie,
    default_axes=True,
    subplots=True,
    labels=labels,
    colors=color_args,
)
assert len(axes) == len(df.columns)

for ax in axes:
    self._check_text_labels(ax.texts, labels)
    self._check_colors(ax.patches, facecolors=color_args)
