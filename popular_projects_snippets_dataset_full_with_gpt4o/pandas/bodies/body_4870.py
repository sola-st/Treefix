# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# PR #1179
s = Series(
    ["A", "B", "C", "Aaba", "Baca", "", np.nan, "CABA", "dog", "cat"],
    dtype=any_string_dtype,
)

result = s.str.contains("a")
expected_dtype = "object" if any_string_dtype == "object" else "boolean"
expected = Series(
    [False, False, False, True, True, False, np.nan, False, False, True],
    dtype=expected_dtype,
)
tm.assert_series_equal(result, expected)

with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    result = s.str.contains("a", case=False)
expected = Series(
    [True, False, False, True, True, False, np.nan, True, False, True],
    dtype=expected_dtype,
)
tm.assert_series_equal(result, expected)

result = s.str.contains("Aa")
expected = Series(
    [False, False, False, True, False, False, np.nan, False, False, False],
    dtype=expected_dtype,
)
tm.assert_series_equal(result, expected)

result = s.str.contains("ba")
expected = Series(
    [False, False, False, True, False, False, np.nan, False, False, False],
    dtype=expected_dtype,
)
tm.assert_series_equal(result, expected)

with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    result = s.str.contains("ba", case=False)
expected = Series(
    [False, False, False, True, True, False, np.nan, True, False, False],
    dtype=expected_dtype,
)
tm.assert_series_equal(result, expected)
