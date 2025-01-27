# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py

tuples = [(0, 1), (1, 2), (3, 4)]
index = IntervalIndex.from_tuples(tuples, closed="right")

result = index.get_indexer(query)
expected = np.array(expected, dtype="intp")
tm.assert_numpy_array_equal(result, expected)
