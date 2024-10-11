# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py

tuples = [(0, 2.5), (1, 3), (2, 4)]
index = IntervalIndex.from_tuples(tuples, closed="left")

result_indexer, result_missing = index.get_indexer_non_unique(query)
expected_indexer = np.array(expected[0], dtype="intp")
expected_missing = np.array(expected[1], dtype="intp")

tm.assert_numpy_array_equal(result_indexer, expected_indexer)
tm.assert_numpy_array_equal(result_missing, expected_missing)
