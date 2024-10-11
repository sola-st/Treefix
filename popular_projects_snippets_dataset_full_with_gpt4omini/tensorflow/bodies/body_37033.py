# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

with self.cached_session():
    n = ops.convert_to_tensor(0)
    c = lambda x: math_ops.less(x, 10)
    b = lambda x: math_ops.add(x, 1)
    r = control_flow_ops.cond(
        math_ops.less(1, 0), lambda: math_ops.add(n, 1),
        lambda: control_flow_ops.while_loop(c, b, [n]))
    self.assertAllEqual(10, self.evaluate(r))
