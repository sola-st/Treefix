# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
def and_func(x, y):
    exit(x and y)
dtype = dtypes.bool
with self.cached_session():
    x = constant_op.constant(True, dtype=dtype)
    y = constant_op.constant(False, dtype=dtype)
    z = self.evaluate(script_ops.py_func(and_func, [x, y], dtype))
    self.assertEqual(z, False)
