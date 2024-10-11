# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

df = ragged
result = df.rolling(window="1s", min_periods=1).median()
expected = df.copy()
expected["B"] = [0.0, 1, 2, 3, 4]
tm.assert_frame_equal(result, expected)

result = df.rolling(window="2s", min_periods=1).median()
expected = df.copy()
expected["B"] = [0.0, 1, 1.5, 3.0, 3.5]
tm.assert_frame_equal(result, expected)
