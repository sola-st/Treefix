# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# Series with non-string values
s = Series(["a", "b", "c", 1.2])
table = str.maketrans("abc", "cde")
expected = Series(["c", "d", "e", np.nan])
result = s.str.translate(table)
tm.assert_series_equal(result, expected)
