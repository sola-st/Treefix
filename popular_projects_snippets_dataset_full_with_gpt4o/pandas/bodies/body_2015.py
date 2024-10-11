# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# https://github.com/pandas-dev/pandas/issues/37262
s = Series(values, dtype=nullable_string_dtype)
result = to_numeric(s)
tm.assert_series_equal(result, expected)
