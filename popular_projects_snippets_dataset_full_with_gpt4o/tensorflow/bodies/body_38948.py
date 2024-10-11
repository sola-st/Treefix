# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.use_gpu():
    for sp_input in (self._SparseTensorValue_5x6(), self._SparseTensor_5x6()):
        sp_output, empty_row_indicator = (
            sparse_ops.sparse_fill_empty_rows(sp_input, -1))

        output, empty_row_indicator_out = self.evaluate(
            [sp_output, empty_row_indicator])

        self.assertAllEqual(
            output.indices,
            [[0, 0], [1, 0], [1, 3], [1, 4], [2, 0], [3, 2], [3, 3], [4, 0]])
        self.assertAllEqual(output.values, [0, 10, 13, 14, -1, 32, 33, -1])
        self.assertAllEqual(output.dense_shape, [5, 6])
        self.assertAllEqual(empty_row_indicator_out,
                            np.array([0, 0, 1, 0, 1]).astype(np.bool_))
