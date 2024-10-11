# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
left = Index([1, 2, 3])
right = Index([True, False])

res = left.get_indexer(right)
expected = -1 * np.ones(len(right), dtype=np.intp)
tm.assert_numpy_array_equal(res, expected)

res = right.get_indexer(left)
expected = -1 * np.ones(len(left), dtype=np.intp)
tm.assert_numpy_array_equal(res, expected)

res = left.get_indexer_non_unique(right)[0]
expected = -1 * np.ones(len(right), dtype=np.intp)
tm.assert_numpy_array_equal(res, expected)

res = right.get_indexer_non_unique(left)[0]
expected = -1 * np.ones(len(left), dtype=np.intp)
tm.assert_numpy_array_equal(res, expected)
