# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
# Not using self.cached_session(), which disables optimization.
with session_lib.Session():
    producer = iter(range(3))
    x, = script_ops.py_func(lambda: next(producer), [], [dtypes.int64])
    self.assertEqual(self.evaluate(x), 0)
    self.assertEqual(self.evaluate(x), 1)
    self.assertEqual(self.evaluate(x), 2)
