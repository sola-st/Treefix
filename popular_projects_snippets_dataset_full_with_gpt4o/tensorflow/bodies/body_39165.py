# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
sp_input = sparse_tensor.SparseTensor.from_value(
    self._SparseTensorValue_2x3x4())
with self.assertRaisesRegex(ValueError, "At most one dimension can"):
    sparse_ops.sparse_reshape(sp_input, shape=(-1, 2, -1))
