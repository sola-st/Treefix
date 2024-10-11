# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_reindex.py
# See GH16770
c = CategoricalIndex([])
res, indexer = c.reindex(["a", "b"])
tm.assert_index_equal(res, Index(["a", "b"]), exact=True)
tm.assert_numpy_array_equal(indexer, np.array([-1, -1], dtype=np.intp))
