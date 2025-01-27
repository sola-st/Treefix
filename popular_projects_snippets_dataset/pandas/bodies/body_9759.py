# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_skew_kurt.py

expected = Series([np.NaN] * 4 + [0.0])[::step]
# yields all NaN (0 variance)
d = Series([1] * 5)
x = d.rolling(window=5, step=step).skew()
# index 4 should be 0 as it contains 5 same obs
tm.assert_series_equal(expected, x)

expected = Series([np.NaN] * 5)[::step]
# yields all NaN (window too small)
d = Series(np.random.randn(5))
x = d.rolling(window=2, step=step).skew()
tm.assert_series_equal(expected, x)

# yields [NaN, NaN, NaN, 0.177994, 1.548824]
d = Series([-1.50837035, -0.1297039, 0.19501095, 1.73508164, 0.41941401])
expected = Series([np.NaN, np.NaN, np.NaN, 0.177994, 1.548824])[::step]
x = d.rolling(window=4, step=step).skew()
tm.assert_series_equal(expected, x)
