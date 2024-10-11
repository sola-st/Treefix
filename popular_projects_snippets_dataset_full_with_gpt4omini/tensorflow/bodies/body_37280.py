# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with context.eager_mode():
    tensor = constant_op.constant(0)
    r = control_flow_ops.while_loop(
        lambda i: i < 3, lambda i: i + 1, [tensor], maximum_iterations=1)
    self.assertEqual(1, r.numpy())
