# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
values = Series(["ab", "AB", "abc", "ABC"], dtype=any_string_dtype)
with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    result = values.str.match("ab", case=False)
expected_dtype = np.bool_ if any_string_dtype == "object" else "boolean"
expected = Series([True, True, True, True], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
