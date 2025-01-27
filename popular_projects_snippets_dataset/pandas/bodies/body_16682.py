# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
result = merge(left, right, how="left", **kwarg)
tm.assert_frame_equal(result, exp)
result = merge(left, right, how="outer", **kwarg)
tm.assert_frame_equal(result, exp)

# TODO: should the next loop be un-indented? doing so breaks this test
for kwarg in [
    {"left_index": True, "right_index": True},
    {"left_index": True, "right_on": "x"},
    {"left_on": "a", "right_index": True},
    {"left_on": "a", "right_on": "x"},
]:
    check1(exp_in, kwarg)
    check2(exp_out, kwarg)
