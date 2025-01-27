# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():
    x = self.evaluate(script_ops.py_func(lambda: 42.0, [], dtypes.float64))
    self.assertAllClose(x, 42.0)
