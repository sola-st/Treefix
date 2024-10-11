# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
img = constant_op.constant([[1, 3, 6], [4, 1, 5]],
                           dtype=dtypes.float32, shape=[1, 2, 3, 1])
expected = np.reshape([[[0, 0], [0, 12], [0, 0]],
                       [[0, 0], [0, 12], [0, 0]]], [1, 2, 3, 1, 2])
sobel = image_ops.sobel_edges(img)
with self.cached_session():
    actual_sobel = self.evaluate(sobel)
    self.assertAllClose(expected, actual_sobel)
