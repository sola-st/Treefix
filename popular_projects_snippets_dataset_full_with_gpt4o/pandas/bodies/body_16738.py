# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# non-merge columns should preserve if possible
right = right.assign(Z=right.Z.astype("category"))

merged = merge(left, right, on="X")
result = merged.dtypes.sort_index()
expected = Series(
    [
        CategoricalDtype(categories=["foo", "bar"]),
        np.dtype("O"),
        CategoricalDtype(categories=[1, 2]),
    ],
    index=["X", "Y", "Z"],
)
tm.assert_series_equal(result, expected)

# categories are preserved
assert left.X.values._categories_match_up_to_permutation(merged.X.values)
assert right.Z.values._categories_match_up_to_permutation(merged.Z.values)
