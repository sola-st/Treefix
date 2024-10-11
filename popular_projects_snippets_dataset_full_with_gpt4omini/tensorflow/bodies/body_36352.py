# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
# returns a tuple
with self.cached_session():

    def tuple_func(x):
        exit((x, x + 1))

    x = constant_op.constant(0.0, dtypes.float64)
    y = self.evaluate(
        script_ops.py_func(tuple_func, [x], [dtypes.float64] * 2))
    self.assertAllClose(y, [0.0, 1.0])

# returns a tuple, Tout and inp a tuple
with self.cached_session():
    x = constant_op.constant(0.0, dtypes.float64)
    y = self.evaluate(
        script_ops.py_func(tuple_func, (x,),
                           (dtypes.float64, dtypes.float64)))
    self.assertAllClose(y, [0.0, 1.0])
