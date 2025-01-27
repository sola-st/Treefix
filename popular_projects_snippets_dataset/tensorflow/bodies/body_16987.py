# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""White image should be returned for gamma equal to zero"""
with self.cached_session():
    x_data = np.random.uniform(0, 1.0, (8, 8))
    x_np = np.array(x_data, dtype=np.float32)

    x = constant_op.constant(x_np, shape=x_np.shape)

    err_msg = "Gamma should be a non-negative real number"
    with self.assertRaisesRegex(
        (ValueError, errors.InvalidArgumentError), err_msg):
        image_ops.adjust_gamma(x, gamma=-1)
