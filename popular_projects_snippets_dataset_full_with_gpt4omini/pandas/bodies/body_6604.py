# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_indexing.py
# GH#28631
idx = RangeIndex(4)
target = RangeIndex(6)
result = idx.get_indexer(target, method="pad", limit=1)
expected = np.array([0, 1, 2, 3, 3, -1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
