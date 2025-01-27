# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    r = control_flow_ops.while_loop(
        lambda i: i < 3, lambda i: i + 1, [0], maximum_iterations=1)
    self.assertEqual(1, self.evaluate(r))
