# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
with self.session() as sess:
    input_val = self._SparseTensorValue_5x6()
    sp_output = sparse_ops.sparse_reshape(input_val, [5, 6])

    output_val = self.evaluate(sp_output)
    self.assertAllEqual(output_val.indices, input_val.indices)
    self.assertAllEqual(output_val.values, input_val.values)
    self.assertAllEqual(output_val.dense_shape, input_val.dense_shape)
