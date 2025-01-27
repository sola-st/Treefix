# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
index = date_range("2020", periods=4, freq="1ns")
df = frame_or_series([1, 1, 1, 1], index=index, dtype=float)
expected = frame_or_series(expected, index=index, dtype=float)
result = df.rolling(window, closed=closed, center=True).sum()
tm.assert_equal(result, expected)
