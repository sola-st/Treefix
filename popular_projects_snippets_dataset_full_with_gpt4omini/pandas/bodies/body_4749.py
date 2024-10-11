# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
values = ["A", np.nan, "¼", "★", np.nan, "３", "four"]
ser = Series(values, dtype=any_string_dtype)
expected_dtype = "object" if any_string_dtype == "object" else "boolean"
expected = Series(expected, dtype=expected_dtype)
result = getattr(ser.str, method)()
tm.assert_series_equal(result, expected)
