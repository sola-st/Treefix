# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session(use_gpu=use_gpu):
    n = constant_op.constant(1.0)
    c = lambda x: math_ops.less(x, 10.0)
    b = lambda x: math_ops.add(x, 1.0)
    r = control_flow_ops.while_loop(c, b, [n])
    self.assertAllClose(10.0, self.evaluate(r))
