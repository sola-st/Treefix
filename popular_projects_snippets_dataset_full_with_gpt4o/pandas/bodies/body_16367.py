# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# https://github.com/pandas-dev/pandas/pull/33846
result = Series("M", index=[1, 2, 3], dtype=nullable_string_dtype)
expected = Series(["M", "M", "M"], index=[1, 2, 3], dtype=nullable_string_dtype)
tm.assert_series_equal(result, expected)
