# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant(0., dtype=dtype)
    y = constant_op.constant(0., dtype=dtype)
    xlogy_xgrad, xlogy_ygrad = self._xlogy_gradients(x, y)
    zero = self.evaluate(x)
    self.assertAllClose(zero, xlogy_xgrad)
    self.assertAllClose(zero, xlogy_ygrad)
