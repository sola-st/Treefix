# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH#48498
arr1 = Series([4, pd.NA], dtype=any_numeric_ea_dtype)
arr2 = Series([1, pd.NA], dtype=any_numeric_ea_dtype)
midx = MultiIndex.from_arrays([arr1, [2, 1]], names=["a", None])
midx2 = MultiIndex.from_arrays([arr2, [1, 2]])
result = midx.union(midx2)
expected = MultiIndex.from_arrays(
    [Series([1, 4, pd.NA, pd.NA], dtype=any_numeric_ea_dtype), [1, 2, 1, 2]]
)
tm.assert_index_equal(result, expected)
