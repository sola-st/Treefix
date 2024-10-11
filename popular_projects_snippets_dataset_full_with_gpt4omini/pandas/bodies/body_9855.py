# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH: 20649
df = DataFrame({"a": [1, 2]})
df["b"] = value
result = df.rolling(window=2, min_periods=1, axis=1).sum()
expected = DataFrame({"a": [1.0, 2.0]})
tm.assert_frame_equal(result, expected)
