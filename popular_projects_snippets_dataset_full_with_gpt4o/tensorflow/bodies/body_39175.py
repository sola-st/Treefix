# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
with self.session() as sess:
    sp_input = self._SparseTensorPlaceholder()
    input_val = self._SparseTensorValue_5x6()
    sp_output = sparse_ops.sparse_reshape(sp_input, [3, -1])

    output_val = sess.run(sp_output, {sp_input: input_val})
    self.assertAllEqual(output_val.indices,
                        np.array([[0, 0], [0, 6], [0, 9], [1, 0], [2, 0],
                                  [2, 1]]))
    self.assertAllEqual(output_val.values, input_val.values)
    self.assertAllEqual(output_val.dense_shape, [3, 10])
