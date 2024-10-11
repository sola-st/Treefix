# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# GH#41760
mi = MultiIndex.from_tuples([("x", "m", "a"), ("x", "n", "b"), ("y", "o", "c")])
df = DataFrame([[1, 2, 3], [4, 5, 6]], columns=mi)
with pytest.raises(KeyError, match="y"):
    df.xs(("x", "y"), drop_level=False, axis=1)
