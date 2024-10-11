# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_check_indexer.py
arr = np.array([1, 2, 3])

msg = "Cannot index with an integer indexer containing NA values"
with pytest.raises(ValueError, match=msg):
    check_array_indexer(arr, indexer)
