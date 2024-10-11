# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py

idx1 = CategoricalIndex(list("aabcde"), categories=list("edabc"))
idx2 = CategoricalIndex(list("abf"))

for indexer in [idx2, list("abf"), Index(list("abf"))]:
    msg = "Reindexing only valid with uniquely valued Index objects"
    with pytest.raises(InvalidIndexError, match=msg):
        idx1.get_indexer(indexer)

    r1, _ = idx1.get_indexer_non_unique(indexer)
    expected = np.array([0, 1, 2, -1], dtype=np.intp)
    tm.assert_almost_equal(r1, expected)
