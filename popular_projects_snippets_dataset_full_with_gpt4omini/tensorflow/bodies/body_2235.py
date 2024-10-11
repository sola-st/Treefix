# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
self.assertAllEqual(
    self._runScatter(array_ops.tensor_scatter_add),
    np.array([1, 10, 1, 10, 10, 1, 1, 10], dtype=np.float32))
