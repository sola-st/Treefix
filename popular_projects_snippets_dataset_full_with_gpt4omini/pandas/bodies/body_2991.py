# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# GH#6399
df = DataFrame(
    [[2, "first"], [2, "second"], [1, "a"], [1, "b"]],
    columns=["sort_col", "order"],
)
sorted_df = df.sort_values(by="sort_col", kind="mergesort", ascending=False)
tm.assert_frame_equal(df, sorted_df)
