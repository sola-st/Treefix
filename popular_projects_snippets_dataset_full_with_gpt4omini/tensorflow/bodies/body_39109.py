# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reorder_op_test.py
expected_output_val = self._SparseTensorValue_5x6(np.arange(6), dtype)
with self.session() as sess:
    for _ in range(5):  # To test various random permutations
        input_val = self._SparseTensorValue_5x6(np.random.permutation(6), dtype)
        sp_output = sparse_ops.sparse_reorder(input_val)

        output_val = self.evaluate(sp_output)
        self.assertAllEqual(output_val.indices, expected_output_val.indices)
        self.assertAllEqual(output_val.values, expected_output_val.values)
        self.assertAllEqual(output_val.dense_shape,
                            expected_output_val.dense_shape)
