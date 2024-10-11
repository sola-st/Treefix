# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_indexing.py
index = RangeIndex(start=0, stop=20, step=2)
target = RangeIndex(10)
indexer = index.get_indexer(target)
expected = np.array([0, -1, 1, -1, 2, -1, 3, -1, 4, -1], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected)
