# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():
    x = constant_op.constant([1.0, 2.0], dtypes.float64)
    y = constant_op.constant([2.0, 3.0], dtypes.float64)
    z = self.evaluate(script_ops.py_func(np_func, [x, y], [dtypes.float64]))
    self.assertAllEqual(z[0],
                        np_func([1.0, 2.0], [2.0, 3.0]).astype(np.float64))
