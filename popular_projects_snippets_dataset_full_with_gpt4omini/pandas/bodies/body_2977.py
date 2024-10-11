# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_diff.py
# GH#32995 operate column-wise when we have mixed dtypes and axis=1
df = DataFrame({"A": range(3), "B": 2 * np.arange(3, dtype=np.float64)})

expected = DataFrame({"A": [np.nan, np.nan, np.nan], "B": df["B"] / 2})

result = df.diff(axis=1)
tm.assert_frame_equal(result, expected)

# GH#21437 mixed-float-dtypes
df = DataFrame(
    {"a": np.arange(3, dtype="float32"), "b": np.arange(3, dtype="float64")}
)
result = df.diff(axis=1)
expected = DataFrame({"a": df["a"] * np.nan, "b": df["b"] * 0})
tm.assert_frame_equal(result, expected)
