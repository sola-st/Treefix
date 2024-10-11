# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_groupby.py
# GH 6279 - SeriesGroupBy histogram can have a legend
index = Index(15 * ["1"] + 15 * ["2"], name="c")
df = DataFrame(np.random.randn(30, 2), index=index, columns=["a", "b"])
g = df.groupby("c")

for ax in g["a"].hist(legend=True):
    self._check_axes_shape(ax, axes_num=1, layout=(1, 1))
    self._check_legend_labels(ax, ["1", "2"])
