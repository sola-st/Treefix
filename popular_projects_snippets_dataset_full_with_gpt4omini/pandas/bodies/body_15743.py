# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_pct_change.py
s = Series([1.0, 1.5, np.nan, 2.5, 3.0])

chg = s.pct_change()
expected = Series([np.nan, 0.5, 0.0, 2.5 / 1.5 - 1, 0.2])
tm.assert_series_equal(chg, expected)
