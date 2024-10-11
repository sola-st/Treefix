# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
indices = np.zeros([1, 1, 2], np.int32)
updates = np.zeros([1, 1], np.int32)
expected = np.zeros([2, 2], dtype=np.int32)
self.assertAllEqual(expected, self._runScatterNd(indices, updates, [2, 2]))
