# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Test case for 10315
x_shapes = [[240, 320, 3], [5, 240, 320, 3]]
expected_y_shapes = [[80, 106, 3], [5, 80, 106, 3]]

for x_shape, y_shape in zip(x_shapes, expected_y_shapes):
    x_np = np.zeros(x_shape, dtype=np.int32)
    y_np = np.zeros(y_shape, dtype=np.int32)
    for use_gpu in [True, False]:
        with self.cached_session(use_gpu=use_gpu):
            y_tf = self.evaluate(image_ops.central_crop(x_np, 0.33))
            self.assertAllEqual(y_tf, y_np)
            self.assertAllEqual(y_tf.shape, y_np.shape)
