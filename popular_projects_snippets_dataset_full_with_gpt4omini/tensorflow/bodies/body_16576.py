# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant(0., dtype=dtype)
    y = constant_op.constant(3.1, dtype=dtype)
    xdivy_xgrad, xdivy_ygrad = self._xdivy_gradients(x, y)
    zero = self.evaluate(x)
    self.assertAllClose(zero, xdivy_xgrad)
    self.assertAllClose(zero, xdivy_ygrad)
