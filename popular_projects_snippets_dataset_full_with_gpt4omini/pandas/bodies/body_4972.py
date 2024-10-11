# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
s = Series([1, 1, 2, np.nan, np.nan])
result = s.mode(dropna)
expected = Series(expected)
tm.assert_series_equal(result, expected)
