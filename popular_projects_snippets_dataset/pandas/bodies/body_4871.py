# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# PR #14171
s = Series([np.nan, np.nan, np.nan], dtype=any_string_dtype)

result = s.str.contains("foo", na=False)
expected_dtype = np.bool_ if any_string_dtype == "object" else "boolean"
expected = Series([False, False, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)

result = s.str.contains("foo", na=True)
expected = Series([True, True, True], dtype=expected_dtype)
tm.assert_series_equal(result, expected)

result = s.str.contains("foo", na="foo")
if any_string_dtype == "object":
    expected = Series(["foo", "foo", "foo"], dtype=np.object_)
else:
    expected = Series([True, True, True], dtype="boolean")
tm.assert_series_equal(result, expected)

result = s.str.contains("foo")
expected_dtype = "object" if any_string_dtype == "object" else "boolean"
expected = Series([np.nan, np.nan, np.nan], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
