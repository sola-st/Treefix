# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with self.cached_session():
    x = constant_op.constant(x_np, shape=x_np.shape)
    y = image_ops.adjust_contrast(x, contrast_factor)
    y_tf = self.evaluate(y)
    self.assertAllClose(y_tf, y_np, 1e-6)
