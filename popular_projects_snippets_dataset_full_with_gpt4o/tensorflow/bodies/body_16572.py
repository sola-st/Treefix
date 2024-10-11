# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant(0.1, dtype=dtype)
    y = constant_op.constant(-1., dtype=dtype)
    xlog1py_xgrad, xlog1py_ygrad = self._xlog1py_gradients(x, y)
    self.assertAllClose(-np.inf, xlog1py_xgrad)
    self.assertAllClose(np.inf, xlog1py_ygrad)
