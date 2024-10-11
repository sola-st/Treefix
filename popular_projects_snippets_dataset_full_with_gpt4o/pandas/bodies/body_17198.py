# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH#48681
df = DataFrame(
    {"a": "A", "b": [1, 2], "sales": Series([10, 11], dtype="Int64")}
)

result = df.pivot_table(index="b", columns="a", margins=True, aggfunc="sum")
expected = DataFrame(
    [[10, 10], [11, 11], [21, 21]],
    index=Index([1, 2, "All"], name="b"),
    columns=MultiIndex.from_tuples(
        [("sales", "A"), ("sales", "All")], names=[None, "a"]
    ),
    dtype="Int64",
)
tm.assert_frame_equal(result, expected)
