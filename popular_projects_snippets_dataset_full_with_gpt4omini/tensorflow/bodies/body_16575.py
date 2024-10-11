# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant(0.1, dtype=dtype)
    y = constant_op.constant(3.1, dtype=dtype)
    xdivy_xgrad, xdivy_ygrad = self._xdivy_gradients(x, y)
    xdivy_expected_xgrad = self.evaluate(1 / y)
    xdivy_expected_ygrad = self.evaluate(-x / y**2)
    self.assertAllClose(xdivy_expected_xgrad, xdivy_xgrad)
    self.assertAllClose(xdivy_expected_ygrad, xdivy_ygrad)
