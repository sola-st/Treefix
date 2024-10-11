# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
sp_input = sparse_tensor.SparseTensor.from_value(
    self._SparseTensorValue_2x3x4())
self.assertAllEqual((2, 3, 4), sp_input.get_shape())
sp_output = sparse_ops.sparse_reshape(sp_input, shape=(2, -1))
self.assertAllEqual((2, 3 * 4), sp_output.get_shape())
