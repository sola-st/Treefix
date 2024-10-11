# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.use_gpu():
    sp_input = self._SparseTensor_2x6()
    sp_output, empty_row_indicator = (
        sparse_ops.sparse_fill_empty_rows(sp_input, -1))

    output, empty_row_indicator_out = self.evaluate(
        [sp_output, empty_row_indicator])

    self.assertAllEqual(output.indices, [[0, 0], [1, 0], [1, 3], [1, 4]])
    self.assertAllEqual(output.values, [0, 10, 13, 14])
    self.assertAllEqual(output.dense_shape, [2, 6])
    self.assertAllEqual(empty_row_indicator_out, np.zeros(2).astype(np.bool_))
