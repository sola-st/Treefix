# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant(0.1, dtype=dtype)
    y = constant_op.constant(3.1, dtype=dtype)
    xlogy_xgrad, xlogy_ygrad = self._xlogy_gradients(x, y)
    xlogy_expected_xgrad = self.evaluate(math_ops.log(y))
    xlogy_expected_ygrad = self.evaluate(x / y)
    self.assertAllClose(xlogy_expected_xgrad, xlogy_xgrad)
    self.assertAllClose(xlogy_expected_ygrad, xlogy_ygrad)
