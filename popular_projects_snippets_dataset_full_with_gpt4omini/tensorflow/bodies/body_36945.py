# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    s = constant_op.constant(0)
    r = isum(s)
    self.assertAllEqual(45, self.evaluate(r))
