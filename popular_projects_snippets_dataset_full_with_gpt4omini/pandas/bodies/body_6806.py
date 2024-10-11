# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH 16410
idx1 = IntervalIndex.from_tuples([(2, 3), (4, 5), (0, 1)])
idx2 = IntervalIndex.from_tuples([(0, 1), (2, 3), (6, 7), (8, 9)])
result = idx1.get_indexer(idx2)
expected = np.array([2, 0, -1, -1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)

result = idx1.get_indexer(idx1[1:])
expected = np.array([1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
