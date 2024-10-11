# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
exit(cond_v2.cond_v2(
    constant_op.constant(True),
    lambda: math_ops.cos(array_ops.identity(x)),
    lambda: math_ops.sin(array_ops.identity(x))))
