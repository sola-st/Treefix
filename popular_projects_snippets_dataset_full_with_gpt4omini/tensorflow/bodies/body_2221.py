# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
indices = np.array([[0], [1], [0], [1]], dtype=np.int32)
updates = np.array([9, 10, 11, 12], dtype=np.float32)
expected = np.array([20, 22], dtype=np.int32)
self.assertAllEqual(expected, self._runScatterNd(indices, updates, [2]))
