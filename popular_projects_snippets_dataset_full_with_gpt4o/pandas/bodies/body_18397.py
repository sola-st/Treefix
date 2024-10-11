# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_interval.py
interval_array = IntervalArray.from_arrays(range(2), range(1, 3), closed=closed)
other = Interval(0, 1, closed=other_closed)

result = op(interval_array, other)
expected = self.elementwise_comparison(op, interval_array, other)
tm.assert_numpy_array_equal(result, expected)
