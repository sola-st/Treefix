# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [13, 9, 3]
x_np = np.arange(0, np.prod(x_shape), dtype=data_type).reshape(x_shape)
y_np = self._NumpyPerImageWhitening(x_np)

with self.cached_session():
    x = constant_op.constant(x_np, dtype=data_type, shape=x_shape)
    y = image_ops.per_image_standardization(x)
    y_tf = self.evaluate(y)
    self.assertAllClose(y_tf, y_np, atol=1e-4)
