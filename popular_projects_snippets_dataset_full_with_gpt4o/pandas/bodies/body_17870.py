# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_extension_array_equal.py
# https://github.com/pandas-dev/pandas/issues/35715
left = array([1, 2, 3], dtype="Int64")
right = array([1, 2, 3], dtype=right_dtype)
tm.assert_extension_array_equal(left, right, check_dtype=False)
