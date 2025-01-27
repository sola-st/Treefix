# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
ret1 = while_loop_v2(
    lambda v: v < 4.,
    lambda v: v * v, [x],
    return_same_structure=False,
    name="while_1")  # x**2
ret2 = while_loop_v2(
    lambda v: v < 16.,
    lambda v: v * v, [x],
    return_same_structure=False,
    name="while_2")  # x**4
exit((ret1, ret2))
