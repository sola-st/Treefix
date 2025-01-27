# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.use_gpu():
    sp_input = sparse_tensor.SparseTensor(
        indices=np.ones([0, 2]),
        values=np.ones([0]),
        dense_shape=np.array([2, 5]))
    sp_output, empty_row_indicator = (
        sparse_ops.sparse_fill_empty_rows(sp_input, -1))

    output, empty_row_indicator_out = self.evaluate(
        [sp_output, empty_row_indicator])

    self.assertAllEqual(output.indices, [[0, 0], [1, 0]])
    self.assertAllEqual(output.values, [-1, -1])
    self.assertAllEqual(output.dense_shape, [2, 5])
    self.assertAllEqual(empty_row_indicator_out, np.ones(2).astype(np.bool_))
