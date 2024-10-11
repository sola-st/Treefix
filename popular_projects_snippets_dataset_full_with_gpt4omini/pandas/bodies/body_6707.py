# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
indexer, missing = tree.get_indexer_non_unique(np.array([1.0, 2.0, 6.5]))

result = indexer[:1]
expected = np.array([0], dtype="intp")
tm.assert_numpy_array_equal(result, expected)

result = np.sort(indexer[1:3])
expected = np.array([0, 1], dtype="intp")
tm.assert_numpy_array_equal(result, expected)

result = np.sort(indexer[3:])
expected = np.array([-1], dtype="intp")
tm.assert_numpy_array_equal(result, expected)

result = missing
expected = np.array([2], dtype="intp")
tm.assert_numpy_array_equal(result, expected)
