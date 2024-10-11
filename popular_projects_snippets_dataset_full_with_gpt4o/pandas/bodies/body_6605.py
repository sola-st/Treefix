# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_indexing.py
# GH#28678
index = RangeIndex(7, stop, -3)
result = index.get_indexer(range(9))
expected = np.array([-1, 2, -1, -1, 1, -1, -1, 0, -1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
