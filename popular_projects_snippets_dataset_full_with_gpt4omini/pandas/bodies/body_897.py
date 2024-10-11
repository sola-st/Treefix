# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_check_indexer.py
# https://github.com/pandas-dev/pandas/issues/31503
arr = np.array([1, 2, 3])

result = check_array_indexer(arr, indexer)
expected = np.array([True, False, False], dtype=bool)

tm.assert_numpy_array_equal(result, expected)
