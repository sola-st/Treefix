# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
input_val = self._SparseTensorValue_5x6()
sp_input = sparse_tensor.SparseTensor.from_value(input_val)
with self.assertRaisesRegex(ValueError, "Cannot reshape"):
    sparse_ops.sparse_reshape(sp_input, [4, 7])
