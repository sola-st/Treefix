# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# PR #10054. xref #7412 and closes #8790.
df1, df2 = dfs_for_indicator
df1_copy = df1.copy()

df2_copy = df2.copy()

df_result = DataFrame(
    {
        "col1": [0, 1, 2, 3, 4, 5],
        "col_conflict_x": [1, 2, np.nan, np.nan, np.nan, np.nan],
        "col_left": ["a", "b", np.nan, np.nan, np.nan, np.nan],
        "col_conflict_y": [np.nan, 1, 2, 3, 4, 5],
        "col_right": [np.nan, 2, 2, 2, 2, 2],
    }
)
df_result["_merge"] = Categorical(
    [
        "left_only",
        "both",
        "right_only",
        "right_only",
        "right_only",
        "right_only",
    ],
    categories=["left_only", "right_only", "both"],
)

df_result = df_result[
    [
        "col1",
        "col_conflict_x",
        "col_left",
        "col_conflict_y",
        "col_right",
        "_merge",
    ]
]

test = merge(df1, df2, on="col1", how="outer", indicator=True)
tm.assert_frame_equal(test, df_result)
test = df1.merge(df2, on="col1", how="outer", indicator=True)
tm.assert_frame_equal(test, df_result)

# No side effects
tm.assert_frame_equal(df1, df1_copy)
tm.assert_frame_equal(df2, df2_copy)

# Check with custom name
df_result_custom_name = df_result
df_result_custom_name = df_result_custom_name.rename(
    columns={"_merge": "custom_name"}
)

test_custom_name = merge(
    df1, df2, on="col1", how="outer", indicator="custom_name"
)
tm.assert_frame_equal(test_custom_name, df_result_custom_name)
test_custom_name = df1.merge(
    df2, on="col1", how="outer", indicator="custom_name"
)
tm.assert_frame_equal(test_custom_name, df_result_custom_name)
