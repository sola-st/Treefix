# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
    x = constant_op.constant(0., dtype=dtype)
    y = constant_op.constant(3.1, dtype=dtype)
    xlog1py_xgrad, xlog1py_ygrad = self._xlog1py_gradients(x, y)
    zero = self.evaluate(x)
    self.assertAllClose(zero, xlog1py_xgrad)
    self.assertAllClose(zero, xlog1py_ygrad)
