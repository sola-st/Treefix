# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

with self.cached_session():
    n = ops.convert_to_tensor(0, name="n")
    c = lambda x: math_ops.less(x, 10)
    b = lambda x: control_flow_ops.cond(constant_op.constant(True), lambda: math_ops.add(x, 1), lambda: n)
    r = control_flow_ops.while_loop(c, b, [n])
    self.assertAllEqual(10, self.evaluate(r))
