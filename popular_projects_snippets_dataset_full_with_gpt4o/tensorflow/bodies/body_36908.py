# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    x = constant_op.constant(0., name="X")
    y = control_flow_ops.cond(
        constant_op.constant(True), lambda: x,
        lambda: control_flow_ops.cond(x < 1., lambda: x, lambda: x))
    result = gradients_impl.gradients(y, x)[0]
    self.assertEqual(1.0, self.evaluate(result))

    z = control_flow_ops.cond(
        constant_op.constant(False), lambda: x,
        lambda: control_flow_ops.cond(x < 1., lambda: x, lambda: x))
    result = gradients_impl.gradients(z, x)[0]
    self.assertEqual(1.0, self.evaluate(result))
