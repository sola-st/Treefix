# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    n = 0
    c = lambda x: x < 10000
    b = lambda x: x + 1
    r = control_flow_ops.while_loop(c, b, [n], parallel_iterations=20)
    self.assertEqual(10000, self.evaluate(r))
