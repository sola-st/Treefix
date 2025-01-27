# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH 17284
index = IntervalIndex.from_tuples([(0, 5)], closed=closed)
result = index.get_indexer([Interval(0, 5, closed)] * size)
expected = np.array([0] * size, dtype="intp")
tm.assert_numpy_array_equal(result, expected)
