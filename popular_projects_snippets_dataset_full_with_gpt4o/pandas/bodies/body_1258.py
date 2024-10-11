# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexers.py
arr = np.zeros(4, dtype=bool)
arr[0] = 1
result = length_of_indexer(arr)
assert result == 1
