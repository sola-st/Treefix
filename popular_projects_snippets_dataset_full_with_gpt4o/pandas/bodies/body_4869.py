# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# https://github.com/pandas-dev/pandas/pull/41025#issuecomment-824062416

values = Series(["a", "b", "c", "a", np.nan], dtype=nullable_string_dtype)
result = values.str.contains("a", na=na, regex=regex)
expected = Series([True, False, False, True, expected], dtype="boolean")
tm.assert_series_equal(result, expected)
