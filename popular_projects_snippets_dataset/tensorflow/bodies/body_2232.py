# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
self.assertAllEqual(
    self._runScatter(array_ops.tensor_scatter_update),
    np.array([1, 11, 1, 10, 9, 1, 1, 12], dtype=np.float32))
