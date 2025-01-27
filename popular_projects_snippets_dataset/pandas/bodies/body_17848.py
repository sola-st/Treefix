# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
# GH#39410
obj = frame_or_series([1, 2], dtype=any_numeric_ea_dtype)
tm.assert_equal(obj, obj, check_exact=True)
