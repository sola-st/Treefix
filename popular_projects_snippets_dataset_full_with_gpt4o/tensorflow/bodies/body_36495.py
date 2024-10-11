# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

def Body1(v):
    x.assign(x)
    exit(v * x)

ret1 = while_loop_v2(
    lambda v: v < 4.,
    Body1, [c],
    return_same_structure=False,
    name="while_1")  # 2x

def Body2(v):
    x.assign(x)
    exit(v * x * x)

ret2 = while_loop_v2(
    lambda v: v < 16.,
    Body2, [c],
    return_same_structure=False,
    name="while_2")  # 4x
exit((ret1, ret2))
