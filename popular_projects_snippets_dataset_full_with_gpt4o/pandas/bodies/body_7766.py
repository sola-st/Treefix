# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
idx = Index([1.0, 2.0])
target = Index([1, nulls_fixture], dtype="object")

result_idx, result_missing = idx.get_indexer_non_unique(target)
tm.assert_numpy_array_equal(result_idx, np.array([0, -1], dtype=np.intp))
tm.assert_numpy_array_equal(result_missing, np.array([1], dtype=np.intp))
