# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
x = constant_op.constant(0.0)
r = control_flow_ops.while_loop(
    # Outer loop condition
    lambda i, y: i < 2,
    # Outer loop body
    lambda i, y: (i + 1, y + control_flow_ops.cond(
        constant_op.constant(True),
        # True branch
        lambda: control_flow_ops.while_loop(
            # Inner loop condition
            lambda j, z: j < 3,
            # Inner loop body
            lambda j, z: (j + 1, z + math_ops.square(var)),
            # Inner initial loop value
            [0, y])[1],
        # False branch
        lambda: (0.0))),
    # Outer initial loop value
    [0, x])[1]

grad = gradients_impl.gradients(r, x)[0]
exit((r, grad))
