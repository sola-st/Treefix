# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 10824
left = DataFrame(columns=["a", "b", "c"])
right = DataFrame(columns=["x", "y", "z"])

exp_in = DataFrame(columns=["a", "b", "c", "x", "y", "z"], dtype=object)

result = merge(left, right, how=join_type, **kwarg)
tm.assert_frame_equal(result, exp_in)
