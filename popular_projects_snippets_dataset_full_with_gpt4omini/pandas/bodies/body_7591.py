# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#49830
midx = MultiIndex.from_arrays(
    [pd.Series([1, 2, 3], dtype=any_numeric_ea_dtype), [10, 11, 12]]
)
midx2 = MultiIndex.from_arrays(
    [pd.Series([5], dtype=any_numeric_ea_dtype), [-1]]
)
result = midx.putmask([True, False, False], midx2)
expected = MultiIndex.from_arrays(
    [pd.Series([5, 2, 3], dtype=any_numeric_ea_dtype), [-1, 11, 12]]
)
tm.assert_index_equal(result, expected)
