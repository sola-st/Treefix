# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
y_np = self._RGBToGrayscale(x_np)

with self.cached_session():
    x_tf = constant_op.constant(x_np, shape=x_np.shape)
    y = image_ops.rgb_to_grayscale(x_tf)
    y_tf = self.evaluate(y)
    self.assertAllEqual(y_tf, y_np)
