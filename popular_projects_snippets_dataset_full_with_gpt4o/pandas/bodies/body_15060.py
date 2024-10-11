# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_groupby.py
# GH 6279 - DataFrameGroupBy histogram can have a legend
expected_layout = (1, expected_axes_num)
expected_labels = column or [["a"], ["b"]]

index = Index(15 * ["1"] + 15 * ["2"], name="c")
df = DataFrame(np.random.randn(30, 2), index=index, columns=["a", "b"])
g = df.groupby("c")

for axes in g.hist(legend=True, column=column):
    self._check_axes_shape(
        axes, axes_num=expected_axes_num, layout=expected_layout
    )
    for ax, expected_label in zip(axes[0], expected_labels):
        self._check_legend_labels(ax, expected_label)
