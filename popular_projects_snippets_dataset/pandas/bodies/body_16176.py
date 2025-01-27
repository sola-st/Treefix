# Extracted from ./data/repos/pandas/pandas/tests/series/test_arithmetic.py
# GH28658 - ensure adding 'm' does not raise an error
a = Series(input_value)

result = a + target_add
expected = Series(expected_value)
tm.assert_series_equal(result, expected)
