# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
updates = np.array([-3, -4, -5]).astype(np.float32)

# Indices all in range, no problem.
indices = np.array([[2], [0], [5]], dtype=np.int32)
self._runScatterNd(indices, updates, [6])

# Indices out of range should not fail. It produces implementation-defined
# output.
indices = np.array([[-1], [0], [5]], dtype=np.int32)
self._runScatterNd(indices, updates, [6])
indices = np.array([[2], [0], [6]], dtype=np.int32)
self._runScatterNd(indices, updates, [6])
