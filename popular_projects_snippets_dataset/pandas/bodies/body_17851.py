# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
# GH#45554
left = DataFrame([[1, 2], [3, 4]])
left.flags.allows_duplicate_labels = False

right = DataFrame([[1, 2], [3, 4]])
right.flags.allows_duplicate_labels = True
tm.assert_frame_equal(left, right, check_flags=False)

with pytest.raises(AssertionError, match="allows_duplicate_labels"):
    tm.assert_frame_equal(left, right, check_flags=True)
