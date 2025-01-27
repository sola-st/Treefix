# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# we have matching Categorical dtypes in X
# so should preserve the merged column
merged = merge(left, right, on="X")
result = merged.dtypes.sort_index()
expected = Series(
    [
        CategoricalDtype(categories=["foo", "bar"]),
        np.dtype("O"),
        np.dtype("int64"),
    ],
    index=["X", "Y", "Z"],
)
tm.assert_series_equal(result, expected)
