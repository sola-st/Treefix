# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# GH 6279 - DataFrame histogram with legend and label raises
index = Index(15 * ["1"] + 15 * ["2"], name="c")
df = DataFrame(np.random.randn(30, 2), index=index, columns=["a", "b"])

with pytest.raises(ValueError, match="Cannot use both legend and label"):
    df.hist(legend=True, by=by, column=column, label="d")
