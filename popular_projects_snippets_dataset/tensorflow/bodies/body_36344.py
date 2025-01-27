# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():
    x = constant_op.constant(1 + 2j, dtypes.complex64)
    y = constant_op.constant(3 + 4j, dtypes.complex64)
    z = self.evaluate(script_ops.py_func(np_func, [x, y], dtypes.complex64))
    self.assertAllClose(z, np_func(1 + 2j, 3 + 4j))
