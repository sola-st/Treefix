# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_reindex.py
# GH41170
idx = MultiIndex.from_arrays(values)
result, result_indexer = idx.reindex(np.array(["b"]), level=0)
expected = MultiIndex(levels=[["b"], values[1]], codes=[[], []])
expected_indexer = np.array([], dtype=result_indexer.dtype)
tm.assert_index_equal(result, expected)
tm.assert_numpy_array_equal(result_indexer, expected_indexer)
