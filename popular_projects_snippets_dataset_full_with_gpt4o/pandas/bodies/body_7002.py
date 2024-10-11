# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_reindex.py
# See GH25459
cat = CategoricalIndex(["a", "b", "c"], categories=["a", "b", "c", "d"])
res, indexer = cat.reindex(["a", "c", "c"])
exp = Index(["a", "c", "c"], dtype="object")
tm.assert_index_equal(res, exp, exact=True)
tm.assert_numpy_array_equal(indexer, np.array([0, 2, 2], dtype=np.intp))

res, indexer = cat.reindex(
    CategoricalIndex(["a", "c", "c"], categories=["a", "b", "c", "d"])
)
exp = CategoricalIndex(["a", "c", "c"], categories=["a", "b", "c", "d"])
tm.assert_index_equal(res, exp, exact=True)
tm.assert_numpy_array_equal(indexer, np.array([0, 2, 2], dtype=np.intp))
