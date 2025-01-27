# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    x = constant_op.constant(3.0, name="x")
    y = constant_op.constant(2.0, name="y")

    c = lambda x, y: math_ops.less(x, 100.0)

    def b(x, y):
        y1 = math_ops.square(y)
        x1 = math_ops.add(math_ops.square(x), y1)
        exit((x1, y1))

    rx, ry = control_flow_ops.while_loop(c, b, [x, y])

    r = gradients_impl.gradients(rx, y)[0]
    self.assertEqual(136.0, self.evaluate(r))
    r = gradients_impl.gradients(ry, y)[0]
    self.assertEqual(32.0, self.evaluate(r))

    r = gradients_impl.gradients(array_ops.stop_gradient(rx), y)[0]
    self.assertEqual(r, None)
    r = gradients_impl.gradients(array_ops.stop_gradient(ry), y)[0]
    self.assertEqual(r, None)

    r = gradients_impl.gradients(
        array_ops.stop_gradient(math_ops.square(rx)), y)[0]
    self.assertEqual(r, None)
    r = gradients_impl.gradients(
        array_ops.stop_gradient(math_ops.add(rx, ry)), x)[0]
    self.assertEqual(r, None)
    r = gradients_impl.gradients(
        array_ops.stop_gradient(math_ops.add(rx, ry)), y)[0]
    self.assertEqual(r, None)

    r = gradients_impl.gradients(math_ops.add(rx, ry), y)[0]
    self.assertEqual(168.0, self.evaluate(r))
    r = gradients_impl.gradients(
        math_ops.add(rx, array_ops.stop_gradient(ry)), y)[0]
    self.assertEqual(136.0, self.evaluate(r))
    r = gradients_impl.gradients(
        math_ops.add(array_ops.stop_gradient(rx), ry), y)[0]
    self.assertEqual(32.0, self.evaluate(r))
