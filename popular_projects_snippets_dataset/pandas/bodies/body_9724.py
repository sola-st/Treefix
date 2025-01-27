# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

df = ragged
result = df.rolling(window="1s", min_periods=1).sum()
expected = df.copy()
expected["B"] = [0.0, 1, 2, 3, 4]
tm.assert_frame_equal(result, expected)

result = df.rolling(window="2s", min_periods=1).sum()
expected = df.copy()
expected["B"] = [0.0, 1, 3, 3, 7]
tm.assert_frame_equal(result, expected)

result = df.rolling(window="2s", min_periods=2).sum()
expected = df.copy()
expected["B"] = [np.nan, np.nan, 3, np.nan, 7]
tm.assert_frame_equal(result, expected)

result = df.rolling(window="3s", min_periods=1).sum()
expected = df.copy()
expected["B"] = [0.0, 1, 3, 5, 7]
tm.assert_frame_equal(result, expected)

result = df.rolling(window="3s").sum()
expected = df.copy()
expected["B"] = [0.0, 1, 3, 5, 7]
tm.assert_frame_equal(result, expected)

result = df.rolling(window="4s", min_periods=1).sum()
expected = df.copy()
expected["B"] = [0.0, 1, 3, 6, 9]
tm.assert_frame_equal(result, expected)

result = df.rolling(window="4s", min_periods=3).sum()
expected = df.copy()
expected["B"] = [np.nan, np.nan, 3, 6, 9]
tm.assert_frame_equal(result, expected)

result = df.rolling(window="5s", min_periods=1).sum()
expected = df.copy()
expected["B"] = [0.0, 1, 3, 6, 10]
tm.assert_frame_equal(result, expected)
