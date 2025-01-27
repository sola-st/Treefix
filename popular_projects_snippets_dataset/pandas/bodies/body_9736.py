# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

df = ragged

result = df.rolling(window="1s", min_periods=1).max()
expected = df.copy()
expected["B"] = [0.0, 1, 2, 3, 4]
tm.assert_frame_equal(result, expected)

result = df.rolling(window="2s", min_periods=1).max()
expected = df.copy()
expected["B"] = [0.0, 1, 2, 3, 4]
tm.assert_frame_equal(result, expected)

result = df.rolling(window="5s", min_periods=1).max()
expected = df.copy()
expected["B"] = [0.0, 1, 2, 3, 4]
tm.assert_frame_equal(result, expected)
