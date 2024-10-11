# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_check_indexer.py
arr = np.array([1, 2, 3])

msg = "arrays used as indices must be of integer or boolean type"
with pytest.raises(IndexError, match=msg):
    check_array_indexer(arr, indexer)
