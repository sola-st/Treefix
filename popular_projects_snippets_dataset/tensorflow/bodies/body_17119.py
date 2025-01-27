# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [13, 9, 3]
x_np = np.ones(x_shape, dtype=np.float32)
for use_gpu in [True, False]:
    with self.cached_session(use_gpu=use_gpu):
        x = constant_op.constant(x_np, shape=x_shape)
        with self.assertRaises(ValueError):
            _ = image_ops.central_crop(x, 0.0)
        with self.assertRaises(ValueError):
            _ = image_ops.central_crop(x, 1.01)
