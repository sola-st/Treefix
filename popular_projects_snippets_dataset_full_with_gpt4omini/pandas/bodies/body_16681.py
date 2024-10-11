# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
result = merge(left, right, how="inner", **kwarg)
tm.assert_frame_equal(result, exp)
result = merge(left, right, how="right", **kwarg)
tm.assert_frame_equal(result, exp)
