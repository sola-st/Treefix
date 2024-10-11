# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_groupby.py
# GH 6279 - DataFrameGroupBy histogram with legend and label raises
index = Index(15 * ["1"] + 15 * ["2"], name="c")
df = DataFrame(np.random.randn(30, 2), index=index, columns=["a", "b"])
g = df.groupby("c")

with pytest.raises(ValueError, match="Cannot use both legend and label"):
    g.hist(legend=True, column=column, label="d")
