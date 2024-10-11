# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shapes = [[13, 9, 3], [5, 13, 9, 3]]
for x_shape in x_shapes:
    x_np = np.ones(x_shape, dtype=np.float32)
    for use_gpu in [True, False]:
        with self.cached_session(use_gpu=use_gpu):
            x = constant_op.constant(x_np, shape=x_shape)
            y = image_ops.central_crop(x, 1.0)
            y_tf = self.evaluate(y)
            self.assertAllEqual(y_tf, x_np)
