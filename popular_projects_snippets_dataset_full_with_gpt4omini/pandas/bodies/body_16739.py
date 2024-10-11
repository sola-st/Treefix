# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# our merging columns, X now has 2 different dtypes
# so we must be object as a result

X = change(right.X.astype("object"))
right = right.assign(X=X)
assert is_categorical_dtype(left.X.values.dtype)
# assert not left.X.values._categories_match_up_to_permutation(right.X.values)

merged = merge(left, right, on="X", how=join_type)

result = merged.dtypes.sort_index()
expected = Series(
    [np.dtype("O"), np.dtype("O"), np.dtype("int64")], index=["X", "Y", "Z"]
)
tm.assert_series_equal(result, expected)
