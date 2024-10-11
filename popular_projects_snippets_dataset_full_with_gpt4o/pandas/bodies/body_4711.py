# Extracted from ./data/repos/pandas/pandas/tests/strings/test_string_array.py
s = Series(["a", None, "1"], dtype=nullable_string_dtype)
result = getattr(s.str, method)()
expected = Series(expected, dtype="boolean")
tm.assert_series_equal(result, expected)
