# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v = constant_op.constant(2.0, name="v")
    c = lambda v: math_ops.less(v, 100.0)
    b = math_ops.square
    r = control_flow_ops.while_loop(c, b, [v], back_prop=False)
    r = math_ops.add(r, v)
    r = gradients_impl.gradients(r, v)
    self.assertAllClose(1.0, r[0])
