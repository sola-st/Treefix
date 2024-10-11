# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH 17284
index = IntervalIndex.from_tuples([(0, 5)], closed=closed)
result = index.get_indexer(item)
expected = np.array([0] * len(item), dtype="intp")
tm.assert_numpy_array_equal(result, expected)
