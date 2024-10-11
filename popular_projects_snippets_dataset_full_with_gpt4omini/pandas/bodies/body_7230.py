# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index = Index(np.arange(10))[::-1]

actual = index.get_indexer([0, 5, 9], method=method)
tm.assert_numpy_array_equal(actual, np.array([9, 4, 0], dtype=np.intp))

actual = index.get_indexer([0.2, 1.8, 8.5], method=method)
tm.assert_numpy_array_equal(actual, np.array(expected, dtype=np.intp))
