# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
batch_size = 5
plane = np.reshape([[1, 3, 6, 2], [4, 1, 5, 7], [2, 5, 1, 4]],
                   [1, 3, 4, 1])
two_channel = np.concatenate([plane, plane], axis=3)
batch = np.concatenate([two_channel] * batch_size, axis=0)
img = constant_op.constant(batch, dtype=dtypes.float32,
                           shape=[batch_size, 3, 4, 2])

expected_plane = np.reshape([[[0, 0], [0, 12], [0, 10], [0, 0]],
                             [[6, 0], [0, 6], [-6, 10], [-6, 0]],
                             [[0, 0], [0, 0], [0, 10], [0, 0]]],
                            [1, 3, 4, 1, 2])
expected_two_channel = np.concatenate(
    [expected_plane, expected_plane], axis=3)
expected_batch = np.concatenate([expected_two_channel] * batch_size, axis=0)

sobel = image_ops.sobel_edges(img)
with self.cached_session():
    actual_sobel = self.evaluate(sobel)
    self.assertAllClose(expected_batch, actual_sobel)
