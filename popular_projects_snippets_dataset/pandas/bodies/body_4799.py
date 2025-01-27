# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
s = Series(data, dtype=any_string_dtype)
result = s.str.capitalize()
expected = Series(expected, dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
