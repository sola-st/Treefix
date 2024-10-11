# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
self.assertAllEqual(
    self._runScatter(array_ops.tensor_scatter_update),
    np.array([1, 9, 1, 9, 9, 1, 1, 9], dtype=np.float32))
