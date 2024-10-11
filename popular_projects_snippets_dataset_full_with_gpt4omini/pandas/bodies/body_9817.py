# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH 42753

index = [
    Timestamp("20130101 09:00:01"),
    Timestamp("20130101 09:00:02"),
    Timestamp("20130101 09:00:02"),
]
df = frame_or_series([1, 1, 1], index=index)

result = df.rolling(window, closed=closed, center=True).sum()
expected = frame_or_series(expected, index=index)
tm.assert_equal(result, expected)
