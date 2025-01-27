# Extracted from ./data/repos/pandas/pandas/tests/copy_view/test_indexing.py
# Case: taking a subset of the rows+columns of a DataFrame using .iloc
# + afterwards modifying the subset
# Generic test for several combinations of row/column indexers, not all
# of those could actually return a view / need CoW (so this test is not
# checking memory sharing, only ensuring subsequent mutation doesn't
# affect the parent dataframe)
df = DataFrame(
    {"a": [1, 2, 3], "b": [4, 5, 6], "c": np.array([7, 8, 9], dtype=dtype)}
)
df_orig = df.copy()

subset = df.iloc[row_indexer, column_indexer]

# modifying the subset never modifies the parent
subset.iloc[0, 0] = 0

expected = DataFrame(
    {"b": [0, 6], "c": np.array([8, 9], dtype=dtype)}, index=range(1, 3)
)
tm.assert_frame_equal(subset, expected)
# a few corner cases _do_ actually modify the parent (with both row and column
# slice, and in case of ArrayManager or BlockManager with single block)
if (
    isinstance(row_indexer, slice)
    and isinstance(column_indexer, slice)
    and (using_array_manager or (dtype == "int64" and not using_copy_on_write))
):
    df_orig.iloc[1, 1] = 0
tm.assert_frame_equal(df, df_orig)
