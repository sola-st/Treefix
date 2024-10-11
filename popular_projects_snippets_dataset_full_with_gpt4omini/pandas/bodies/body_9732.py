# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

df = ragged
result = df.rolling(window="1s", min_periods=1).count()
expected = df.copy()
expected["B"] = [1.0, 1, 1, 1, 1]
tm.assert_frame_equal(result, expected)

df = ragged
result = df.rolling(window="1s").count()
tm.assert_frame_equal(result, expected)

result = df.rolling(window="2s", min_periods=1).count()
expected = df.copy()
expected["B"] = [1.0, 1, 2, 1, 2]
tm.assert_frame_equal(result, expected)

result = df.rolling(window="2s", min_periods=2).count()
expected = df.copy()
expected["B"] = [np.nan, np.nan, 2, np.nan, 2]
tm.assert_frame_equal(result, expected)
