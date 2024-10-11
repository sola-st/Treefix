# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_split_op_test.py
for sp_input in (self._SparseTensorValue_3x4x2(),
                 self._SparseTensor_3x4x2()):
    for axis in (1, -2):
        sparse_tensors = sparse_ops.sparse_split(
            sp_input=sp_input, num_split=2, axis=axis)
        concat_tensor = self.evaluate(
            sparse_ops.sparse_concat(1, sparse_tensors))
        expected_output = self._SparseTensor_3x4x2()
        self.assertAllEqual(concat_tensor.indices, expected_output.indices)
