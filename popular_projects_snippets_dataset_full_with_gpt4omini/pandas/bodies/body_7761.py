# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
# GH#48411
idx = Index([1, 2, NA, NA], dtype="Int64")
result = idx.get_indexer_for(Index([1, NA], dtype="Int64"))
expected = np.array([0, 2, 3], dtype=result.dtype)
tm.assert_numpy_array_equal(result, expected)
