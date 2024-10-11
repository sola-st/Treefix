# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_interval.py
# matches first interval
other = interval_array[0]
result = op(interval_array, other)
expected = self.elementwise_comparison(op, interval_array, other)
tm.assert_numpy_array_equal(result, expected)

# matches on a single endpoint but not both
other = Interval(interval_array.left[0], interval_array.right[1])
result = op(interval_array, other)
expected = self.elementwise_comparison(op, interval_array, other)
tm.assert_numpy_array_equal(result, expected)
