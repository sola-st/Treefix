# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reorder_op_test.py
sp_input = sparse_tensor.SparseTensor.from_value(
    self._SparseTensorValue_5x6(np.arange(6)))
self.assertAllEqual((5, 6), sp_input.get_shape())
sp_output = sparse_ops.sparse_reorder(sp_input)
self.assertAllEqual((5, 6), sp_output.get_shape())
