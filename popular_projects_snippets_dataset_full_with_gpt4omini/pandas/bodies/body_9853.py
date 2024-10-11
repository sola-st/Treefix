# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH: 20649
df = DataFrame(1, index=[1, 2], columns=["a", "b", "c"])
df["c"] = 1.0
result = getattr(df.rolling(window=2, min_periods=1, axis=1), func)()
expected = DataFrame(
    {"a": [1.0, 1.0], "b": [value, value], "c": [value, value]},
    index=[1, 2],
)
tm.assert_frame_equal(result, expected)
