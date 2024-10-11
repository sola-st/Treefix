# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with test_util.use_gpu():
    sp_input = sparse_tensor.SparseTensor(
        indices=np.ones([0, 2]),
        values=np.ones([0]),
        dense_shape=np.array([0, 3]))
    sp_output, empty_row_indicator = (
        sparse_ops.sparse_fill_empty_rows(sp_input, -1))

    output, empty_row_indicator_out = self.evaluate(
        [sp_output, empty_row_indicator])

    self.assertAllEqual(output.indices, np.ones([0, 2]))
    self.assertAllEqual(output.values, np.ones([0]))
    self.assertAllEqual(output.dense_shape, [0, 3])
    self.assertAllEqual(empty_row_indicator_out, [])
