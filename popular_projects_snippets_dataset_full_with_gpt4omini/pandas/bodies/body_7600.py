# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#37222
idx1 = MultiIndex.from_product([["A"], [1.0, 2.0]], names=["id1", "id2"])
idx2 = MultiIndex.from_product([["A"], [np.nan, 2.0]], names=["id1", "id2"])
expected = np.array([-1, 1])
result = idx2.get_indexer(idx1)
tm.assert_numpy_array_equal(result, expected, check_dtype=False)
result = idx1.get_indexer(idx2)
tm.assert_numpy_array_equal(result, expected, check_dtype=False)
