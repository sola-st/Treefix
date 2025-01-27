# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_index_as_string.py

# Construct expected result
expected = compute_expected(
    left_df, right_df, left_on=left_on, right_on=right_on, how=how
)

# Perform merge
result = left_df.merge(right_df, left_on=left_on, right_on=right_on, how=how)
tm.assert_frame_equal(result, expected, check_like=True)
