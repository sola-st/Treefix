# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
indices = np.array([[4], [3], [1], [7]], dtype=np.int32)
updates = np.array([9, 10, 11, 12], dtype=np.float32)
expected = np.array([0, 11, 0, 10, 9, 0, 0, 12], dtype=np.int32)
self.assertAllEqual(expected, self._runScatterNd(indices, updates, [8]))
