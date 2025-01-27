# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 15193
categories = ["a", "b", "c", "d"]

df = DataFrame(
    {
        "A": ["a", "a", "a", "b", "b", "b", "c", "c", "c"],
        "B": [1, 2, 3, 1, 2, 3, 1, 2, 3],
        "C": range(0, 9),
    }
)

df["A"] = df["A"].astype(CDT(categories, ordered=False))
result = df.pivot_table(index="B", columns="A", values="C", dropna=dropna)
expected_columns = Series(["a", "b", "c"], name="A")
expected_columns = expected_columns.astype(CDT(categories, ordered=False))
expected_index = Series([1, 2, 3], name="B")
expected = DataFrame(
    [[0, 3, 6], [1, 4, 7], [2, 5, 8]],
    index=expected_index,
    columns=expected_columns,
)
if not dropna:
    # add back the non observed to compare
    expected = expected.reindex(columns=Categorical(categories)).astype("float")

tm.assert_frame_equal(result, expected)
