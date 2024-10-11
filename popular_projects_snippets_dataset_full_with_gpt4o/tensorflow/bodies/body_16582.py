# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
for dtype in [dtypes.float32, dtypes.float64]:
    x1 = constant_op.constant(0.1, dtype=dtype)
    x2 = constant_op.constant(3.1, dtype=dtype)
    dx1, dx2 = self._nextafter_gradient(x1, x2)
    expected_dx1 = constant_op.constant(1, dtype=dtype)
    expected_dx2 = constant_op.constant(0, dtype=dtype)
    self.assertAllClose(expected_dx1, dx1)
    self.assertAllClose(expected_dx2, dx2)
