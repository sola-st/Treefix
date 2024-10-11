# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_values.py
# GH#38426 Clarify sort_values with mult. columns / labels is stable
df = DataFrame(
    {
        "A": [1, 2, np.nan, 1, 1, 1, 6, 8, 4, 8, 8, np.nan, np.nan, 8, 8],
        "B": [9, np.nan, 5, 2, 2, 2, 5, 4, 5, 3, 4, np.nan, np.nan, 4, 4],
    }
)
# All rows with NaN in col "B" only have unique values in "A", therefore,
# only the rows with NaNs in "A" have to be treated individually:
expected_idx = (
    [11, 12, 2] + expected_idx_non_na
    if na_position == "first"
    else expected_idx_non_na + [2, 11, 12]
)
expected = df.take(expected_idx)
sorted_df = df.sort_values(
    ["A", "B"], ascending=ascending, na_position=na_position
)
tm.assert_frame_equal(sorted_df, expected)
