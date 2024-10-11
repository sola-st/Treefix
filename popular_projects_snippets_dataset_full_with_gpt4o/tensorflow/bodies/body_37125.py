# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
exit(control_flow_ops.while_loop(
    lambda i, _: i < 3,
    lambda i, x: (i + 1, control_flow_ops.cond(
        constant_op.constant(True),
        lambda: x + var,
        lambda: x)),
    [0, 0.0])[1])
