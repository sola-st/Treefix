# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
sp_input = sparse_tensor.SparseTensor.from_value(
    self._SparseTensorValue_5x6())
self.assertAllEqual((5, 6), sp_input.get_shape())
sp_output = sparse_ops.sparse_reshape(sp_input, shape=(1, 5, 2, 3))
self.assertAllEqual((1, 5, 2, 3), sp_output.get_shape())
