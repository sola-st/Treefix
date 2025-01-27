# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_interval.py
# same endpoints
other = interval_constructor(interval_array.left, interval_array.right)
result = op(interval_array, other)
expected = self.elementwise_comparison(op, interval_array, other)
tm.assert_equal(result, expected)

# different endpoints
other = interval_constructor(
    interval_array.left[::-1], interval_array.right[::-1]
)
result = op(interval_array, other)
expected = self.elementwise_comparison(op, interval_array, other)
tm.assert_equal(result, expected)

# all nan endpoints
other = interval_constructor([np.nan] * 4, [np.nan] * 4)
result = op(interval_array, other)
expected = self.elementwise_comparison(op, interval_array, other)
tm.assert_equal(result, expected)
