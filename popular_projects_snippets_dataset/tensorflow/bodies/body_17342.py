# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
shape = [1, 2, 4, 1]
img = constant_op.constant([[1, 3, 4, 2], [8, 7, 5, 6]])
img = array_ops.reshape(img, shape)

expected_dy = np.reshape([[7, 4, 1, 4], [0, 0, 0, 0]], shape)
expected_dx = np.reshape([[2, 1, -2, 0], [-1, -2, 1, 0]], shape)

dy, dx = image_ops.image_gradients(img)
with self.cached_session():
    actual_dy = self.evaluate(dy)
    actual_dx = self.evaluate(dx)
    self.assertAllClose(expected_dy, actual_dy)
    self.assertAllClose(expected_dx, actual_dx)
