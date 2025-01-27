# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH#47477
df = DataFrame({"x": "a", "y": "b", "age": Series([20, 40], dtype="Int64")})
result = df.pivot_table(
    index="x", columns="y", values="age", aggfunc="mean", dropna=dropna
)
expected = DataFrame(
    [[30]],
    index=Index(["a"], name="x"),
    columns=Index(["b"], name="y"),
    dtype="Float64",
)
tm.assert_frame_equal(result, expected)
