# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():
    val = [[1, 2], [3, 4]]
    x, = script_ops.py_func(lambda: np.array(val, order="F"), [],
                            [dtypes.int64])
    self.assertAllEqual(val, self.evaluate(x))
