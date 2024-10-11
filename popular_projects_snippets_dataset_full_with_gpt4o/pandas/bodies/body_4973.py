# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# Test string and object types.
data = ["a"] * 2 + ["b"] * 3

s = Series(data, dtype="c")
result = s.mode(dropna)
expected1 = Series(expected1, dtype="c")
tm.assert_series_equal(result, expected1)

data = ["foo", "bar", "bar", np.nan, np.nan, np.nan]

s = Series(data, dtype=object)
result = s.mode(dropna)
expected2 = Series(expected2, dtype=object)
tm.assert_series_equal(result, expected2)

data = ["foo", "bar", "bar", np.nan, np.nan, np.nan]

s = Series(data, dtype=object).astype(str)
result = s.mode(dropna)
expected3 = Series(expected3, dtype=str)
tm.assert_series_equal(result, expected3)
