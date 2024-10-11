# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH: 32724
df = DataFrame({"A": [1, None], "B": [4, 5], "C": [7, 8]})
expected = DataFrame({"A": [1.0, np.nan], "B": [5.0, 5.0], "C": [11.0, 13.0]})
result = df.rolling(min_periods=1, window=2, axis=1).sum()
tm.assert_frame_equal(result, expected)

result = df.T.rolling(min_periods=1, window=2).sum().T
tm.assert_frame_equal(result, expected)
