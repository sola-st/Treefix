# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
s = Series(["FOO", "BAR", np.nan, "Blah", "blurg"], dtype=any_string_dtype)
result = s.str.swapcase()
expected = Series(["foo", "bar", np.nan, "bLAH", "BLURG"], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
