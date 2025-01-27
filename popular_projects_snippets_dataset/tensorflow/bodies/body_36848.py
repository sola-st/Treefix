# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

with self.cached_session():
    x = constant_op.constant(10)
    r = control_flow_ops.cond(
        math_ops.less(1, 0), lambda: math_ops.add(x, 1),
        lambda: math_ops.subtract(x, 1))
    result = self.evaluate(r)
self.assertAllEqual(9, result)
