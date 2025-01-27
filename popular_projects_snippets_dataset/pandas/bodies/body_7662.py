# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# GH26408
# test if codes are re-assigned value -1 for levels
# with missing values (NaN, NaT, None)
result = MultiIndex(
    levels=[[np.nan, None, pd.NaT, 128, 2]], codes=[[0, -1, 1, 2, 3, 4]]
)
expected = MultiIndex(
    levels=[[np.nan, None, pd.NaT, 128, 2]], codes=[[-1, -1, -1, -1, 3, 4]]
)
tm.assert_index_equal(result, expected)

result = MultiIndex(
    levels=[[np.nan, "s", pd.NaT, 128, None]], codes=[[0, -1, 1, 2, 3, 4]]
)
expected = MultiIndex(
    levels=[[np.nan, "s", pd.NaT, 128, None]], codes=[[-1, -1, 1, -1, 3, -1]]
)
tm.assert_index_equal(result, expected)

# verify set_levels and set_codes
result = MultiIndex(
    levels=[[1, 2, 3, 4, 5]], codes=[[0, -1, 1, 2, 3, 4]]
).set_levels([[np.nan, "s", pd.NaT, 128, None]])
tm.assert_index_equal(result, expected)

result = MultiIndex(
    levels=[[np.nan, "s", pd.NaT, 128, None]], codes=[[1, 2, 2, 2, 2, 2]]
).set_codes([[0, -1, 1, 2, 3, 4]])
tm.assert_index_equal(result, expected)
