# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH#46560
kernel = arithmetic_win_operators
df = DataFrame({"a": [1], "b": 2, "c": 3})
df["c"] = df["c"].astype(object)
rolling = df.rolling(2, min_periods=1)
op = getattr(rolling, kernel)
result = op(numeric_only=numeric_only)

columns = ["a", "b"] if numeric_only else ["a", "b", "c"]
expected = df[columns].agg([kernel]).reset_index(drop=True).astype(float)
assert list(expected.columns) == columns

tm.assert_frame_equal(result, expected)
