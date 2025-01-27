# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant(0.1, dtype=dtype)
    y = constant_op.constant(0., dtype=dtype)
    xdivy_xgrad, xdivy_ygrad = self._xdivy_gradients(x, y)
    self.assertAllClose(np.inf, xdivy_xgrad)
    self.assertAllClose(-np.inf, xdivy_ygrad)
