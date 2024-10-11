# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
result = merge(
    left_df, right_df, left_index=True, right_index=True, how=how, sort=sort
)
tm.assert_frame_equal(result, expected)
