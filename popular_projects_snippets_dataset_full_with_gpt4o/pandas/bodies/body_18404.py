# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_interval.py
result = op(interval_array, other)
expected = self.elementwise_comparison(op, interval_array, other)
tm.assert_numpy_array_equal(result, expected)
