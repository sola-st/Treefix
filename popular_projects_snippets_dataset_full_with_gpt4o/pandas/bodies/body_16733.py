# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# merging on the same, should preserve dtypes
merged = merge(left, left, on="X")
result = merged.dtypes.sort_index()
expected = Series(
    [CategoricalDtype(categories=["foo", "bar"]), np.dtype("O"), np.dtype("O")],
    index=["X", "Y_x", "Y_y"],
)
tm.assert_series_equal(result, expected)
