# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# https://github.com/pandas-dev/pandas/pull/24809
s = Series(["a", "b", "ac", np.nan, ""], dtype=any_string_dtype)
result = s.str.replace("^.$", "a", regex=True)
expected = Series(["a", "a", "ac", np.nan, ""], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
