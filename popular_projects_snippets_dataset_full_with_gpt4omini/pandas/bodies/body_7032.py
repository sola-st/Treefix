# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
# GH 45361
ci = CategoricalIndex([1, 2, np.nan, 3])
other1 = [2, 3, 4, np.nan]
res1 = ci.get_indexer(other1)
expected1 = np.array([1, 3, -1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(res1, expected1)
other2 = [1, 4, 2, 3]
res2 = ci.get_indexer(other2)
expected2 = np.array([0, -1, 1, 3], dtype=np.intp)
tm.assert_numpy_array_equal(res2, expected2)
