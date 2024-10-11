# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# GH #6609
s = Series(["a", "b", np.nan], dtype=any_string_dtype)

result = s.str.match("a", na=False)
expected_dtype = np.bool_ if any_string_dtype == "object" else "boolean"
expected = Series([True, False, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)

result = s.str.match("a")
expected_dtype = "object" if any_string_dtype == "object" else "boolean"
expected = Series([True, False, np.nan], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
