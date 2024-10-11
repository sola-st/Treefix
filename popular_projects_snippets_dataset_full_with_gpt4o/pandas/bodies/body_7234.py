# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
idx = Index([0.0, 1.0, 2.0], dtype=np.float64)
tm.assert_numpy_array_equal(
    idx.get_indexer(idx), np.array([0, 1, 2], dtype=np.intp)
)

target = [-0.1, 0.5, 1.1]
tm.assert_numpy_array_equal(
    idx.get_indexer(target, "pad"), np.array([-1, 0, 1], dtype=np.intp)
)
tm.assert_numpy_array_equal(
    idx.get_indexer(target, "backfill"), np.array([0, 1, 2], dtype=np.intp)
)
tm.assert_numpy_array_equal(
    idx.get_indexer(target, "nearest"), np.array([0, 1, 1], dtype=np.intp)
)
