# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 24893
df = DataFrame(
    {
        "A": [2, 4, 6, 8],
        "B": [1, 4, 5, 8],
        "C": [1, 3, 4, 6],
        "D": ["X", "X", "Y", "Y"],
    }
)

result = pivot_table(df, index="D", margins=True)
expected = DataFrame(
    {"A": [3, 7, 5], "B": [2.5, 6.5, 4.5], "C": [2, 5, 3.5]},
    index=Index(["X", "Y", "All"], name="D"),
)
tm.assert_frame_equal(result, expected)
