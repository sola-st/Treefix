# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
breaks = np.arange(1, 11, dtype=np.int64)
expected = IntervalIndex.from_breaks(breaks, closed=closed)
result = self.create_index(closed=closed).delete(0)
tm.assert_index_equal(result, expected)
