# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
s = Series([1, "foo", "foo"])
result = s.mode(dropna)
expected = Series(expected1)
tm.assert_series_equal(result, expected)

s = Series([1, "foo", "foo", np.nan, np.nan, np.nan])
result = s.mode(dropna)
expected = Series(expected2, dtype=object)
tm.assert_series_equal(result, expected)
