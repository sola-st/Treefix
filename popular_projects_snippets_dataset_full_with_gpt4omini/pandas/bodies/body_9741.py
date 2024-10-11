# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py
# GH16058

idx = date_range("2017-01-01", periods=24, freq="1h")
ss = Series(np.arange(len(idx)), index=idx)

result = ss.rolling("2h").cov()
expected = Series([np.nan] + [0.5] * (len(idx) - 1), index=idx)
tm.assert_series_equal(result, expected)

expected2 = ss.rolling(2, min_periods=1).cov()
tm.assert_series_equal(result, expected2)

result = ss.rolling("3h").cov()
expected = Series([np.nan, 0.5] + [1.0] * (len(idx) - 2), index=idx)
tm.assert_series_equal(result, expected)

expected2 = ss.rolling(3, min_periods=1).cov()
tm.assert_series_equal(result, expected2)
