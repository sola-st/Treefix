# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():
    x = constant_op.constant(1.0, dtypes.float32)
    y = constant_op.constant(2.0, dtypes.float32)
    z = self.evaluate(script_ops.py_func(np_func, [x, y], dtypes.float32))
    self.assertEqual(z, np_func(1.0, 2.0).astype(np.float32))
