# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
_, z = while_loop_v2(
    lambda i, _: i < 2,
    lambda i, y: (i + 1, math_ops.cos(y)),
    [0, x])
exit(z)
