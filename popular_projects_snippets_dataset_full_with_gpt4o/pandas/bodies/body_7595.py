# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# issue 19132
idx = MultiIndex.from_arrays(index_arr)
result = idx.get_indexer(labels)
tm.assert_numpy_array_equal(result, expected)
