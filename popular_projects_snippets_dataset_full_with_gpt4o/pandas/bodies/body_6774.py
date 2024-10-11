# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
index = self.create_index(closed=closed)

result = index.sort_values()
tm.assert_index_equal(result, index)

result = index.sort_values(ascending=False)
tm.assert_index_equal(result, index[::-1])

# with nan
index = IntervalIndex([Interval(1, 2), np.nan, Interval(0, 1)])

result = index.sort_values()
expected = IntervalIndex([Interval(0, 1), Interval(1, 2), np.nan])
tm.assert_index_equal(result, expected)

result = index.sort_values(ascending=False, na_position="first")
expected = IntervalIndex([np.nan, Interval(1, 2), Interval(0, 1)])
tm.assert_index_equal(result, expected)
