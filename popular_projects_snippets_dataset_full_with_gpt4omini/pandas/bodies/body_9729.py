# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py

df = ragged
result = df.rolling(window="1s", min_periods=1).var(ddof=0)
expected = df.copy()
expected["B"] = [0.0] * 5
tm.assert_frame_equal(result, expected)

result = df.rolling(window="1s", min_periods=1).var(ddof=1)
expected = df.copy()
expected["B"] = [np.nan] * 5
tm.assert_frame_equal(result, expected)

result = df.rolling(window="3s", min_periods=1).var(ddof=0)
expected = df.copy()
expected["B"] = [0.0] + [0.25] * 4
tm.assert_frame_equal(result, expected)

result = df.rolling(window="5s", min_periods=1).var(ddof=1)
expected = df.copy()
expected["B"] = [np.nan, 0.5, 1.0, 1.0, 1 + 2 / 3.0]
tm.assert_frame_equal(result, expected)
