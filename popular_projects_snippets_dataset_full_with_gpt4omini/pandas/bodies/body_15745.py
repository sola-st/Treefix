# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_pct_change.py
# GH30463
s = Series([np.nan, 1, 2, 3, 9, 18], index=["a", "b"] * 3)
result = s.pct_change(fill_method=fill_method)
expected = Series([np.nan, np.nan, 1.0, 0.5, 2.0, 1.0], index=["a", "b"] * 3)
tm.assert_series_equal(result, expected)
