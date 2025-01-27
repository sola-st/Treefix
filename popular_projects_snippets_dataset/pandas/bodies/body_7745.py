# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_join.py
# GH#49830
midx = MultiIndex.from_arrays(
    [Series([1, 2], dtype=any_numeric_ea_dtype), [np.nan, np.nan]]
)
midx2 = MultiIndex.from_arrays(
    [Series([1, 0, 0], dtype=any_numeric_ea_dtype), [np.nan, np.nan, np.nan]]
)
result = midx.join(midx2, how="outer")
expected = MultiIndex.from_arrays(
    [
        Series([0, 0, 1, 2], dtype=any_numeric_ea_dtype),
        [np.nan, np.nan, np.nan, np.nan],
    ]
)
tm.assert_index_equal(result, expected)
