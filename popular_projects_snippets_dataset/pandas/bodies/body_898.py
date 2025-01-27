# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_check_indexer.py
arr = np.array([1, 2, 3])

msg = "Boolean index has wrong length"
with pytest.raises(IndexError, match=msg):
    check_array_indexer(arr, indexer)
