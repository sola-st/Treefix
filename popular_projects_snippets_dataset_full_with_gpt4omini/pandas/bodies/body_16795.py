# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_ordered.py
# GH 35269
result = merge_ordered(
    left=left,
    right=right,
    on=on,
    left_by=left_by,
    right_by=right_by,
)

tm.assert_frame_equal(result, expected)
