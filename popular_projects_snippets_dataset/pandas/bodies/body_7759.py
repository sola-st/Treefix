# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py

if index._index_as_unique:
    expected = np.arange(index.size, dtype=np.intp)
    actual = index.get_indexer(index)
    tm.assert_numpy_array_equal(expected, actual)
else:
    msg = "Reindexing only valid with uniquely valued Index objects"
    with pytest.raises(InvalidIndexError, match=msg):
        index.get_indexer(index)

with pytest.raises(ValueError, match="Invalid fill method"):
    index.get_indexer(index, method="invalid")
