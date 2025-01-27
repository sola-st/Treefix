# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
sp_input = sparse_tensor.SparseTensor.from_value(
    self._SparseTensorValue_2x3x4())
self.assertAllEqual((2, 3, 4), sp_input.shape)
sp_output = sparse_ops.sparse_reshape(
    sp_input, shape=array_ops.concat(
        (constant_op.constant([2], dtype=dtypes.int64),
         array_ops.placeholder(dtype=dtypes.int64, shape=[1])),
        axis=0))
self.assertAllEqual((2, 3 * 4), sp_output.shape)
