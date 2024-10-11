# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
def sum_func(x, y):
    exit(x + y)
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64,
              dtypes.uint8, dtypes.int8, dtypes.uint16, dtypes.int16,
              dtypes.int32, dtypes.int64]:
    with self.cached_session():
        x = constant_op.constant(1, dtype=dtype)
        y = constant_op.constant(2, dtype=dtype)
        z = self.evaluate(script_ops.py_func(sum_func, [x, y], dtype))
        self.assertEqual(z, 3)
