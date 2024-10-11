# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Verifying the output with expected results for gamma

    correction for float32 images
    """
with self.cached_session():
    x_np = np.random.uniform(0, 1.0, (8, 8))
    x = constant_op.constant(x_np, shape=x_np.shape)
    y = image_ops.adjust_gamma(x, gamma=gamma)
    y_tf = self.evaluate(y)

    y_np = np.clip(np.power(x_np, gamma), 0, 1.0)

    self.assertAllClose(y_tf, y_np, 1e-6)
