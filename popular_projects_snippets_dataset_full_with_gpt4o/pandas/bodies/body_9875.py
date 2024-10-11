# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH#41053
df = DataFrame([0.002, 0.008, 0.005, np.NaN, np.NaN, np.NaN])
result = df.rolling(3, min_periods=0).sum()
expected = DataFrame([0.002, 0.010, 0.015, 0.013, 0.005, 0.0])
tm.assert_frame_equal(result, expected)
