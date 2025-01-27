# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_indexing.py
# GH#25459
indexes, missing = Index(["A", "B"]).get_indexer_non_unique(Index([0]))
tm.assert_numpy_array_equal(np.array([-1], dtype=np.intp), indexes)
tm.assert_numpy_array_equal(np.array([0], dtype=np.intp), missing)
