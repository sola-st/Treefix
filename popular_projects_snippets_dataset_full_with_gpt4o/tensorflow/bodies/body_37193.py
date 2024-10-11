# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    x = constant_op.constant(2.0, name="x")
    y = constant_op.constant(2.0, name="y")

    c = lambda x: math_ops.less(x, 100.0)
    b = lambda x: math_ops.multiply(x, y)
    rx = control_flow_ops.while_loop(c, b, [x])

    rg = gradients_impl.gradients(rx, y)[0]
    rg = array_ops.stop_gradient(rg)
    r = math_ops.add(math_ops.square(y), rx)
    r = math_ops.add(r, rg)
    r = gradients_impl.gradients(r, y)[0]
    self.assertEqual(388.0, self.evaluate(r))
