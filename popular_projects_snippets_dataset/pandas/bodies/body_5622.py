# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# https://github.com/pandas-dev/pandas/issues/22205
s = np.tile(1.0, 1_000_001)
series = Series(s)
s[0] = np.nan
result = series.isin([np.nan, 1])
expected = Series(np.ones(len(s), dtype=bool))
tm.assert_series_equal(result, expected)
