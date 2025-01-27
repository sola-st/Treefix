# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
# https://github.com/pandas-dev/pandas/issues/35715
left = DataFrame({"a": [1, 2, 3]}, dtype="Int64")
right = DataFrame({"a": [1, 2, 3]}, dtype=right_dtype)
tm.assert_frame_equal(left, right, check_dtype=False)
