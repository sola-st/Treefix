# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
self.assertAllEqual(
    self._runScatter(array_ops.tensor_scatter_add),
    np.array([1, 12, 1, 11, 10, 1, 1, 13], dtype=np.float32))
