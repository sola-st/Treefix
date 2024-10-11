# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py

def Body1(v):
    x1.assign(x1)
    exit(v * x1)

ret1 = while_loop_v2(
    lambda v: v < 4.,
    Body1, [c],
    return_same_structure=False,
    name="while_1")  # 2x

def Body2(v):
    x1.assign(x1)
    exit(v * x1 * x1)

ret2 = while_loop_v2(
    lambda v: v < 16.,
    Body2, [c],
    return_same_structure=False,
    name="while_2")  # 4x

def Body3(v):
    x2.assign(x2)
    exit(v * x2)

ret3 = while_loop_v2(
    lambda v: v < 4.,
    Body3, [c],
    return_same_structure=False,
    name="while_3")  # 3x

def Body4(v):
    x2.assign(x2)
    exit(v * x2 * x2)

ret4 = while_loop_v2(
    lambda v: v < 16.,
    Body4, [c],
    return_same_structure=False,
    name="while_4")  # 9x
ret5 = while_loop_v2(
    lambda v: v < 16.,
    lambda v: v * v, [c],
    return_same_structure=False,
    name="while_stateless")  # x**2
exit((ret1, ret2, ret3, ret4, ret5))
