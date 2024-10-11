# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py

left_multi = left_multi.drop(columns=left_multi.columns)
right_multi = right_multi.drop(columns=right_multi.columns)

expected = (
    merge(
        left_multi.reset_index(),
        right_multi.reset_index(),
        how=join_type,
        on=on_cols_multi,
    )
    .set_index(idx_cols_multi)
    .sort_index()
)

result = left_multi.join(right_multi, how=join_type).sort_index()
tm.assert_frame_equal(result, expected)
