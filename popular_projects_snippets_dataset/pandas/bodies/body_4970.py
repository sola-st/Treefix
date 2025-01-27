# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
s = Series([], dtype=np.float64)
result = s.mode(dropna)
tm.assert_series_equal(result, expected)
