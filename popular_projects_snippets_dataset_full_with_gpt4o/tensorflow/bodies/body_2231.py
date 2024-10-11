# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scatter_nd_op_test.py
self.assertAllEqual(
    self._runScatter(array_ops.tensor_scatter_sub),
    np.array([1, -10, 1, -9, -8, 1, 1, -11], dtype=np.float32))
