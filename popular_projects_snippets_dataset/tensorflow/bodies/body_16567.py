# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant(0.1, dtype=dtype)
    y = constant_op.constant(0., dtype=dtype)
    xlogy_xgrad, xlogy_ygrad = self._xlogy_gradients(x, y)
    self.assertAllClose(-np.inf, xlogy_xgrad)
    self.assertAllClose(np.inf, xlogy_ygrad)
