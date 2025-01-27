# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
ser = Series(["ab", "AB", "abc", "ABC"], dtype=any_string_dtype)
expected_dtype = np.bool_ if any_string_dtype == "object" else "boolean"

expected = Series([True, False, False, False], dtype=expected_dtype)

result = ser.str.fullmatch("ab", case=True)
tm.assert_series_equal(result, expected)

expected = Series([True, True, False, False], dtype=expected_dtype)

with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    result = ser.str.fullmatch("ab", case=False)
tm.assert_series_equal(result, expected)

with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    result = ser.str.fullmatch("ab", flags=re.IGNORECASE)
tm.assert_series_equal(result, expected)
