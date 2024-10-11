# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    s = constant_op.constant([1, 2, 3, 4, 5])
    r = isum(s, maximum_iterations=3)
    self.assertAllEqual([1 + 3, 2 + 3, 3 + 3, 4 + 3, 5 + 3], self.evaluate(r))
