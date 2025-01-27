# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Verifying the output with expected results for gamma

    correction for uint8 images
    """
with self.cached_session():
    x_np = np.random.uniform(0, 255, (8, 8)).astype(np.uint8)
    x = constant_op.constant(x_np, shape=x_np.shape)
    y = image_ops.adjust_gamma(x, gamma=gamma)
    y_tf = np.trunc(self.evaluate(y))

    # calculate gamma correction using numpy
    # firstly, transform uint8 to float representation
    # then perform correction
    y_np = np.power(x_np / 255.0, gamma)
    # convert correct numpy image back to uint8 type
    y_np = np.trunc(np.clip(y_np * 255.5, 0, 255.0))

    self.assertAllClose(y_tf, y_np, 1e-6)
