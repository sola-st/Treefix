# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

df = ragged
result = df.rolling(window="3s", min_periods=1).skew()
expected = df.copy()
expected["B"] = [np.nan] * 5
tm.assert_frame_equal(result, expected)

result = df.rolling(window="5s", min_periods=1).skew()
expected = df.copy()
expected["B"] = [np.nan] * 2 + [0.0, 0.0, 0.0]
tm.assert_frame_equal(result, expected)
