# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
with self.session() as sess:
    sp_input = self._SparseTensorPlaceholder()
    input_val = self._SparseTensorValue_5x6()
    shape = array_ops.shape(sp_input)  # tf.shape generates int32 output
    sp_output = sparse_ops.sparse_reshape(sp_input, shape)

    output_val = sess.run(sp_output, {sp_input: input_val})
    self.assertAllEqual(output_val.indices, input_val.indices)
    self.assertAllEqual(output_val.values, input_val.values)
    self.assertAllEqual(output_val.dense_shape, input_val.dense_shape)
