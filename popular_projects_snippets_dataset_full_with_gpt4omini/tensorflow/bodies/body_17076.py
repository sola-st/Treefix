# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
x_np = np.array(
    [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]],
    dtype=np.uint8).reshape([2, 2, 3, 1])

y_np = np.array(
    [[[1, 4], [2, 5], [3, 6]], [[7, 10], [8, 11], [9, 12]]],
    dtype=np.uint8).reshape([2, 3, 2, 1])

with self.cached_session():
    x_tf = constant_op.constant(x_np, shape=x_np.shape)
    y = image_ops.transpose(x_tf)
    y_tf = self.evaluate(y)
    self.assertAllEqual(y_tf, y_np)
