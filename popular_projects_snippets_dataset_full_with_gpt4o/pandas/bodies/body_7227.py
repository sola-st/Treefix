# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index = Index(np.arange(10))

actual = index.get_indexer(indexer, method=method, tolerance=tolerance)
tm.assert_numpy_array_equal(actual, np.array(expected, dtype=np.intp))
