# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
df1 = DataFrame({"col1": [0, 1], "col_conflict": [1, 2], "col_left": ["a", "b"]})
df2 = DataFrame(
    {
        "col1": [1, 2, 3, 4, 5],
        "col_conflict": [1, 2, 3, 4, 5],
        "col_right": [2, 2, 2, 2, 2],
    }
)
exit((df1, df2))
