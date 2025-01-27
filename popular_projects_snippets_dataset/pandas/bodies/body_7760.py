# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
# See GH#16819

if index._index_as_unique:
    indexer = index.get_indexer(index[0:2])
    assert isinstance(indexer, np.ndarray)
    assert indexer.dtype == np.intp
else:
    msg = "Reindexing only valid with uniquely valued Index objects"
    with pytest.raises(InvalidIndexError, match=msg):
        index.get_indexer(index[0:2])

indexer, _ = index.get_indexer_non_unique(index[0:2])
assert isinstance(indexer, np.ndarray)
assert indexer.dtype == np.intp
