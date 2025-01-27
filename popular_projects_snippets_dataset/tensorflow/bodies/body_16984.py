# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# 4-D input with batch dimension.
x_np = np.array([[1, 2]], dtype=np.uint8).reshape([1, 1, 2, 1])
y_np = np.array(
    [[1, 1, 1], [2, 2, 2]], dtype=np.uint8).reshape([1, 1, 2, 3])

with self.cached_session():
    x_tf = constant_op.constant(x_np, shape=x_np.shape)
    y = image_ops.grayscale_to_rgb(x_tf)
    y_tf = self.evaluate(y)
    self.assertAllEqual(y_tf, y_np)

# 3-D input with no batch dimension.
x_np = np.array([[1, 2]], dtype=np.uint8).reshape([1, 2, 1])
y_np = np.array([[1, 1, 1], [2, 2, 2]], dtype=np.uint8).reshape([1, 2, 3])

with self.cached_session():
    x_tf = constant_op.constant(x_np, shape=x_np.shape)
    y = image_ops.grayscale_to_rgb(x_tf)
    y_tf = self.evaluate(y)
    self.assertAllEqual(y_tf, y_np)
