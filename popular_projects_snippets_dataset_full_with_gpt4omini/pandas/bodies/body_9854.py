# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH: 35596
df = DataFrame(
    [
        [0, 1, 2, 4, np.nan, np.nan, np.nan],
        [0, 1, 2, np.nan, np.nan, np.nan, np.nan],
        [0, 2, 2, np.nan, 2, np.nan, 1],
    ]
)
result = df.rolling(window=7, min_periods=1, axis="columns").sum()
expected = DataFrame(
    [
        [0.0, 1.0, 3.0, 7.0, 7.0, 7.0, 7.0],
        [0.0, 1.0, 3.0, 3.0, 3.0, 3.0, 3.0],
        [0.0, 2.0, 4.0, 4.0, 6.0, 6.0, 7.0],
    ]
)
tm.assert_frame_equal(result, expected)
