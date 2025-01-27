# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_shape = [4, 8, 1]
x_np = np.array(
    [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8],
     [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]],
    dtype=np.int32).reshape(x_shape)
y_np = np.array([[3, 4, 5, 6], [3, 4, 5, 6]]).reshape([2, 4, 1])
for use_gpu in [True, False]:
    with self.cached_session(use_gpu=use_gpu):
        x = constant_op.constant(x_np, shape=x_shape)
        y = image_ops.central_crop(x, 0.5)
        y_tf = self.evaluate(y)
        self.assertAllEqual(y_tf, y_np)
        self.assertAllEqual(y_tf.shape, y_np.shape)

x_shape = [2, 4, 8, 1]
x_np = np.array(
    [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8],
     [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8],
     [8, 7, 6, 5, 4, 3, 2, 1], [8, 7, 6, 5, 4, 3, 2, 1],
     [8, 7, 6, 5, 4, 3, 2, 1], [8, 7, 6, 5, 4, 3, 2, 1]],
    dtype=np.int32).reshape(x_shape)
y_np = np.array([[[3, 4, 5, 6], [3, 4, 5, 6]],
                 [[6, 5, 4, 3], [6, 5, 4, 3]]]).reshape([2, 2, 4, 1])
with self.cached_session():
    x = constant_op.constant(x_np, shape=x_shape)
    y = image_ops.central_crop(x, 0.5)
    y_tf = self.evaluate(y)
    self.assertAllEqual(y_tf, y_np)
    self.assertAllEqual(y_tf.shape, y_np.shape)
