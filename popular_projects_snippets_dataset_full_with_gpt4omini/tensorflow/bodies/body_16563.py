# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
x_vals = [0, 1.0, np.nan, np.inf, np.NINF]
x = constant_op.constant(x_vals, dtype=dtypes.float32)
y = array_ops.zeros_like(x, dtype=dtypes.float32)
outputs = math_ops.mul_no_nan(x, y)
with self.cached_session():
    dx, dy = gradients.gradients(outputs, [x, y])
    self.assertAllClose(dx, np.zeros(x.shape.as_list()))
    self.assertAllClose(dy, x_vals)
