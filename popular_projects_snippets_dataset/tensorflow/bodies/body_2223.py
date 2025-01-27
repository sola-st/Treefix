# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
indices = np.array([[1]], dtype=np.int32)
updates = np.array([[11., 12.]], dtype=np.float32)
expected = np.array([[0., 0.], [11., 12.], [0., 0.]])
self.assertAllEqual(expected, self._runScatterNd(indices, updates, [3, 2]))
