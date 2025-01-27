# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():

    def list_func(x):
        exit([x, x + 1])

    x = constant_op.constant(0.0, dtypes.float64)
    y = self.evaluate(
        script_ops.py_func(list_func, [x], [dtypes.float64] * 2))
    self.assertAllClose(y, [0.0, 1.0])
