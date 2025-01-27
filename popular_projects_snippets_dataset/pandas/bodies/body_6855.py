# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_base.py
index = self.create_index(closed=closed)

result = index.take(range(10))
tm.assert_index_equal(result, index)

result = index.take([0, 0, 1])
expected = IntervalIndex.from_arrays([0, 0, 1], [1, 1, 2], closed=closed)
tm.assert_index_equal(result, expected)
