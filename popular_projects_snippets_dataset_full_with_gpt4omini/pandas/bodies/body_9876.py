# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 22719
s = Series(range(1))
result = s.rolling(0).min()
expected = Series([np.nan])
tm.assert_series_equal(result, expected)
