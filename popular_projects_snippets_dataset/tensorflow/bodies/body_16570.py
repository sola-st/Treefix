# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant(0.1, dtype=dtype)
    y = constant_op.constant(3.1, dtype=dtype)
    xlog1py_xgrad, xlog1py_ygrad = self._xlog1py_gradients(x, y)
    xlog1py_expected_xgrad = self.evaluate(math_ops.log1p(y))
    xlog1py_expected_ygrad = self.evaluate(x / (1. + y))
    self.assertAllClose(xlog1py_expected_xgrad, xlog1py_xgrad)
    self.assertAllClose(xlog1py_expected_ygrad, xlog1py_ygrad)
