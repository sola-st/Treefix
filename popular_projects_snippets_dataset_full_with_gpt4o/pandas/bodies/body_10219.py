# Extracted from ./data/repos/pandas/pandas/tests/window/test_pairwise.py
# GH 31789
s = Series(range(5), index=date_range("2020", periods=5))
result = s.rolling("12H").corr(s)
expected = Series([np.nan] * 5, index=date_range("2020", periods=5))
tm.assert_series_equal(result, expected)
