# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
values = np.array(
    ["foo", np.nan, "fooommm__foo", "mmm_", "foommm[_]+bar"], dtype=np.object_
)
values = Series(values, dtype=any_string_dtype)
pat = "mmm[_]+"

result = values.str.contains(pat)
expected_dtype = "object" if any_string_dtype == "object" else "boolean"
expected = Series(
    np.array([False, np.nan, True, True, False], dtype=np.object_),
    dtype=expected_dtype,
)
tm.assert_series_equal(result, expected)

result = values.str.contains(pat, regex=False)
expected = Series(
    np.array([False, np.nan, False, False, True], dtype=np.object_),
    dtype=expected_dtype,
)
tm.assert_series_equal(result, expected)

values = Series(
    np.array(["foo", "xyz", "fooommm__foo", "mmm_"], dtype=object),
    dtype=any_string_dtype,
)
result = values.str.contains(pat)
expected_dtype = np.bool_ if any_string_dtype == "object" else "boolean"
expected = Series(np.array([False, False, True, True]), dtype=expected_dtype)
tm.assert_series_equal(result, expected)

# case insensitive using regex
values = Series(
    np.array(["Foo", "xYz", "fOOomMm__fOo", "MMM_"], dtype=object),
    dtype=any_string_dtype,
)
with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    result = values.str.contains("FOO|mmm", case=False)
expected = Series(np.array([True, False, True, True]), dtype=expected_dtype)
tm.assert_series_equal(result, expected)

# case insensitive without regex
result = values.str.contains("foo", regex=False, case=False)
expected = Series(np.array([True, False, True, False]), dtype=expected_dtype)
tm.assert_series_equal(result, expected)

# unicode
values = Series(
    np.array(["foo", np.nan, "fooommm__foo", "mmm_"], dtype=np.object_),
    dtype=any_string_dtype,
)
pat = "mmm[_]+"

result = values.str.contains(pat)
expected_dtype = "object" if any_string_dtype == "object" else "boolean"
expected = Series(
    np.array([False, np.nan, True, True], dtype=np.object_), dtype=expected_dtype
)
tm.assert_series_equal(result, expected)

result = values.str.contains(pat, na=False)
expected_dtype = np.bool_ if any_string_dtype == "object" else "boolean"
expected = Series(np.array([False, False, True, True]), dtype=expected_dtype)
tm.assert_series_equal(result, expected)

values = Series(
    np.array(["foo", "xyz", "fooommm__foo", "mmm_"], dtype=np.object_),
    dtype=any_string_dtype,
)
result = values.str.contains(pat)
expected = Series(np.array([False, False, True, True]), dtype=expected_dtype)
tm.assert_series_equal(result, expected)
