# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reorder_op_test.py
with self.session() as sess:
    sp_input = self._SparseTensorPlaceholder()
    input_val = self._SparseTensorValue_5x6(np.arange(6))
    sp_output = sparse_ops.sparse_reorder(sp_input)

    output_val = sess.run(sp_output, {sp_input: input_val})
    self.assertAllEqual(output_val.indices, input_val.indices)
    self.assertAllEqual(output_val.values, input_val.values)
    self.assertAllEqual(output_val.dense_shape, input_val.dense_shape)
