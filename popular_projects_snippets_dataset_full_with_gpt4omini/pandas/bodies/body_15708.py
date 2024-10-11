# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_compare.py
index = pd.MultiIndex.from_arrays([[0, 0, 1], [0, 1, 2]])
s1 = pd.Series(["a", "b", "c"], index=index)
s2 = pd.Series(["x", "b", "z"], index=index)

result = s1.compare(s2, align_axis=0)

indices = pd.MultiIndex.from_arrays(
    [[0, 0, 1, 1], [0, 0, 2, 2], ["self", "other", "self", "other"]]
)
expected = pd.Series(["a", "x", "c", "z"], index=indices)
tm.assert_series_equal(result, expected)
