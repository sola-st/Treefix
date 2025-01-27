# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH#3917

# Test DataFrame with nan label
df = DataFrame(
    {"A": [1, 2, np.nan, 1, 6, 8, 4], "B": [9, np.nan, 5, 2, 5, 4, 5]},
    index=[1, 2, 3, 4, 5, 6, np.nan],
)

# NaN label, ascending=True, na_position='last'
sorted_df = df.sort_index(kind="quicksort", ascending=True, na_position="last")
expected = DataFrame(
    {"A": [1, 2, np.nan, 1, 6, 8, 4], "B": [9, np.nan, 5, 2, 5, 4, 5]},
    index=[1, 2, 3, 4, 5, 6, np.nan],
)
tm.assert_frame_equal(sorted_df, expected)

# NaN label, ascending=True, na_position='first'
sorted_df = df.sort_index(na_position="first")
expected = DataFrame(
    {"A": [4, 1, 2, np.nan, 1, 6, 8], "B": [5, 9, np.nan, 5, 2, 5, 4]},
    index=[np.nan, 1, 2, 3, 4, 5, 6],
)
tm.assert_frame_equal(sorted_df, expected)

# NaN label, ascending=False, na_position='last'
sorted_df = df.sort_index(kind="quicksort", ascending=False)
expected = DataFrame(
    {"A": [8, 6, 1, np.nan, 2, 1, 4], "B": [4, 5, 2, 5, np.nan, 9, 5]},
    index=[6, 5, 4, 3, 2, 1, np.nan],
)
tm.assert_frame_equal(sorted_df, expected)

# NaN label, ascending=False, na_position='first'
sorted_df = df.sort_index(
    kind="quicksort", ascending=False, na_position="first"
)
expected = DataFrame(
    {"A": [4, 8, 6, 1, np.nan, 2, 1], "B": [5, 4, 5, 2, 5, np.nan, 9]},
    index=[np.nan, 6, 5, 4, 3, 2, 1],
)
tm.assert_frame_equal(sorted_df, expected)
