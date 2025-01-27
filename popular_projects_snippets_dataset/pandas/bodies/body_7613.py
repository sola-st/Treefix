# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# issue 19132
idx = MultiIndex.from_product([[np.nan, 1]] * 2)
expected = slice(0, 2, None)
assert idx.get_loc(np.nan) == expected

idx = MultiIndex.from_arrays([[np.nan, 1, 2, np.nan]])
expected = np.array([True, False, False, True])
tm.assert_numpy_array_equal(idx.get_loc(np.nan), expected)

idx = MultiIndex.from_product([[np.nan, 1]] * 3)
expected = slice(2, 4, None)
assert idx.get_loc((np.nan, 1)) == expected
