# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

df = regular.copy()

df.index = date_range("20130101", periods=5, freq="D")
expected = df.rolling(window=1, min_periods=1).sum()
result = df.rolling(window="1D").sum()
tm.assert_frame_equal(result, expected)

df.index = date_range("20130101", periods=5, freq="2D")
expected = df.rolling(window=1, min_periods=1).sum()
result = df.rolling(window="2D", min_periods=1).sum()
tm.assert_frame_equal(result, expected)

expected = df.rolling(window=1, min_periods=1).sum()
result = df.rolling(window="2D", min_periods=1).sum()
tm.assert_frame_equal(result, expected)

expected = df.rolling(window=1).sum()
result = df.rolling(window="2D").sum()
tm.assert_frame_equal(result, expected)
