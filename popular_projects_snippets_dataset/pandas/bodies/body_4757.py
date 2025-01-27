# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(["abcb", "ab", "bcbe", np.nan], dtype=any_string_dtype)
expected_dtype = np.float64 if any_string_dtype == "object" else "Int64"

result = getattr(ser.str, method)("b")
expected = Series(exp + [np.nan], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
