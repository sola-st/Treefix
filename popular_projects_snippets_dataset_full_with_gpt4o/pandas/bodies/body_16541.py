# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py
on_cols = ["key1", "key2"]
result = left.join(right, on=on_cols, how=join_type).reset_index(drop=True)

expected = merge(left, right.reset_index(), on=on_cols, how=join_type)

tm.assert_frame_equal(result, expected)

result = left.join(right, on=on_cols, how=join_type, sort=True).reset_index(
    drop=True
)

expected = merge(
    left, right.reset_index(), on=on_cols, how=join_type, sort=True
)

tm.assert_frame_equal(result, expected)
