# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# GH 6279 - DataFrame histogram can have a legend
expected_axes_num = 1 if by is None and column is not None else 2
expected_layout = (1, expected_axes_num)
expected_labels = column or ["a", "b"]
if by is not None:
    expected_labels = [expected_labels] * 2

index = Index(15 * ["1"] + 15 * ["2"], name="c")
df = DataFrame(np.random.randn(30, 2), index=index, columns=["a", "b"])

# Use default_axes=True when plotting method generate subplots itself
axes = _check_plot_works(
    df.hist,
    default_axes=True,
    legend=True,
    by=by,
    column=column,
)

self._check_axes_shape(axes, axes_num=expected_axes_num, layout=expected_layout)
if by is None and column is None:
    axes = axes[0]
for expected_label, ax in zip(expected_labels, axes):
    self._check_legend_labels(ax, expected_label)
