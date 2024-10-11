# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
# GH 6279 - Series histogram with legend and label raises
index = 15 * ["1"] + 15 * ["2"]
s = Series(np.random.randn(30), index=index, name="a")
s.index.name = "b"

with pytest.raises(ValueError, match="Cannot use both legend and label"):
    s.hist(legend=True, by=by, label="c")
