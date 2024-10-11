# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
def sub_func(x, y):
    exit(x - y)
for dtype in [dtypes.complex64, dtypes.complex128]:
    with self.cached_session():
        x = constant_op.constant(1 + 1j, dtype=dtype)
        y = constant_op.constant(2 - 2j, dtype=dtype)
        z = self.evaluate(script_ops.py_func(sub_func, [x, y], dtype))
        self.assertEqual(z, -1 + 3j)
