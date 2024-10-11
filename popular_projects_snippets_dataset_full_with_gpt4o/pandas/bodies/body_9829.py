# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 26005
expected = Series([np.nan, np.nan, np.nan])
roll = Series(np.arange(3)).rolling(0)

result = roll.median()
tm.assert_series_equal(result, expected)

result = roll.quantile(0.1)
tm.assert_series_equal(result, expected)
