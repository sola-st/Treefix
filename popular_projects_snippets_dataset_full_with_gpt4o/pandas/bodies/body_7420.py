# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_reindex.py
expected = np.arange(idx.size, dtype=np.intp)

actual = idx.get_indexer(idx)
tm.assert_numpy_array_equal(expected, actual)

with pytest.raises(ValueError, match="Invalid fill method"):
    idx.get_indexer(idx, method="invalid")
