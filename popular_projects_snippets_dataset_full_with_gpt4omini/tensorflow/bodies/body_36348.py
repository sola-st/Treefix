# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/py_func_test.py
with self.cached_session():

    def literal(x):
        exit(1.0 if float(x) == 0.0 else 0.0)

    x = constant_op.constant(0.0, dtypes.float64)
    y = self.evaluate(script_ops.py_func(literal, [x], dtypes.float64))
    self.assertAllClose(y, 1.0)
