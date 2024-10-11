# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
prod = constant_op.constant(1.)
exit((i - 1., previous_sum + while_loop_v2(
    lambda c, _: c > 0,
    lambda c, v: (c - 1., v * n), [i, prod],
    return_same_structure=False)[1]))
