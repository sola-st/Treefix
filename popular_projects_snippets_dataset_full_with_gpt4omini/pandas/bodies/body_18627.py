# Extracted from ./data/repos/pandas/pandas/tests/libs/test_lib.py
indexer = np.array([-1, -1, 1, 2, 0, -1, 3, 4], dtype=np.intp)
result = lib.get_reverse_indexer(indexer, 5)
expected = np.array([4, 2, 3, 6, 7], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
