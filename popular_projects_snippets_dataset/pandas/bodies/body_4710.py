# Extracted from ./data/repos/pandas/pandas/tests/strings/test_string_array.py
s = Series(["aba", None], dtype=nullable_string_dtype)
result = getattr(s.str, method)("a")
expected = Series(expected, dtype="Int64")
tm.assert_series_equal(result, expected)
