# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH#48607
midx = MultiIndex.from_arrays(
    [Series([1, 2], dtype=any_numeric_ea_dtype), [2, 1]], names=["a", None]
)
midx2 = MultiIndex.from_arrays(
    [Series([1, 2, val], dtype=any_numeric_ea_dtype), [1, 1, 3]]
)
result = midx.symmetric_difference(midx2)
expected = MultiIndex.from_arrays(
    [Series([1, 1, val], dtype=any_numeric_ea_dtype), [1, 2, 3]]
)
tm.assert_index_equal(result, expected)
