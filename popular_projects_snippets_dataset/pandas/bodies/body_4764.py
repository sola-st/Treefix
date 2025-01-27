# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(["xxABCxx", "xx BNSD", "LDFJH xx"], dtype=any_string_dtype)

result = getattr(ser.str, method)("x")
expected = Series(exp, dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
