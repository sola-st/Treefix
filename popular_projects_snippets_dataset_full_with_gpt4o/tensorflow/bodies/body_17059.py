# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_np = np.array([[1, 2, 3], [1, 2, 3]], dtype=np.uint8).reshape([2, 3, 1])
y_np = np.array([[3, 2, 1], [3, 2, 1]], dtype=np.uint8).reshape([2, 3, 1])

with self.cached_session():
    x_tf = constant_op.constant(x_np, shape=x_np.shape)
    y = image_ops.flip_left_right(x_tf)
    y_tf = self.evaluate(y)
    self.assertAllEqual(y_tf, y_np)
