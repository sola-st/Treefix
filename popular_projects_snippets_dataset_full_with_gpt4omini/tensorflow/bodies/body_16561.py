# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad_test.py
x = constant_op.constant(np.arange(-3, 3),
                         dtype=dtypes.float32)
y = array_ops.zeros_like(x,
                         dtype=dtypes.float32)
outputs = math_ops.div_no_nan(x, y)
with self.cached_session():
    dx, dy = gradients.gradients(outputs, [x, y])
    self.assertAllClose(dx, np.zeros(x.shape.as_list()))
    self.assertAllClose(dy, np.zeros(y.shape.as_list()))
