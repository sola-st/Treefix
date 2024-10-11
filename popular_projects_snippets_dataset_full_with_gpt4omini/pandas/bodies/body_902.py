# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_check_indexer.py
arr = np.array([1, 2, 3])

result = check_array_indexer(arr, indexer)
assert result == indexer
