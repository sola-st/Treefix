# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_interval.py
other = [nulls_fixture] * 4
result = op(interval_array, other)
expected = self.elementwise_comparison(op, interval_array, other)

tm.assert_equal(result, expected)
