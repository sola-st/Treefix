# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH-19551
df1 = DataFrame(
    {
        "Foo": Categorical(["A", "B", "C"], categories=["A", "B", "C"]),
        "Left": ["A0", "B0", "C0"],
    }
)

df2 = DataFrame(
    {
        "Foo": Categorical(["C", "B", "A"], categories=["C", "B", "A"]),
        "Right": ["C1", "B1", "A1"],
    }
)
result = merge(df1, df2, on=["Foo"])
expected = DataFrame(
    {
        "Foo": Categorical(["A", "B", "C"]),
        "Left": ["A0", "B0", "C0"],
        "Right": ["A1", "B1", "C1"],
    }
)
tm.assert_frame_equal(result, expected)
