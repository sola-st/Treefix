# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
index = IntervalIndex.from_tuples([(0, 1), (2, 3)], closed=closed)
target = [0.5, 1.5, 2.5]
actual = index.get_indexer(target)
expected = np.array([0, -1, 1], dtype="intp")
tm.assert_numpy_array_equal(actual, expected)

assert 1.5 not in index
