# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# https://github.com/pandas-dev/pandas/issues/41602
ser = Series(["A.", "a.", "Ab", "ab", np.nan], dtype=any_string_dtype)

with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    result = ser.str.replace("a", "c", case=False, regex=False)
expected = Series(["c.", "c.", "cb", "cb", np.nan], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)

with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    result = ser.str.replace("a.", "c.", case=False, regex=False)
expected = Series(["c.", "c.", "Ab", "ab", np.nan], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
