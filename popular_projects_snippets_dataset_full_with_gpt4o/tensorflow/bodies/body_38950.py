# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
with self.session():
    values = constant_op.constant(
        [0.0, 10.0, 13.0, 14.0, 32.0, 33.0], dtype=dtypes.float64)
    default_value = constant_op.constant(-1.0, dtype=dtypes.float64)
    sp_input = sparse_tensor.SparseTensorValue(
        indices=np.array([[0, 0], [1, 0], [1, 3], [1, 4], [3, 2], [3, 3]]),
        values=values,
        dense_shape=np.array([5, 6]))
    sp_output, empty_row_indicator = (sparse_ops.sparse_fill_empty_rows(
        sp_input, default_value))
    output, empty_row_indicator_out = self.evaluate(
        [sp_output, empty_row_indicator])

    self.assertAllEqual(output.indices, [[0, 0], [1, 0], [1, 3], [1, 4],
                                         [2, 0], [3, 2], [3, 3], [4, 0]])
    self.assertAllClose(output.values, [0, 10, 13, 14, -1, 32, 33, -1])
    self.assertAllEqual(output.dense_shape, [5, 6])
    self.assertAllEqual(empty_row_indicator_out,
                        np.array([0, 0, 1, 0, 1]).astype(np.bool_))

    values_grad_err = gradient_checker.compute_gradient_error(
        values, values.shape.as_list(), sp_output.values, [8], delta=1e-8)
    self.assertGreater(values_grad_err, 0)
    self.assertLess(values_grad_err, 1e-8)

    default_value_grad_err = gradient_checker.compute_gradient_error(
        default_value,
        default_value.shape.as_list(),
        sp_output.values, [8],
        delta=1e-8)
    self.assertGreater(default_value_grad_err, 0)
    self.assertLess(default_value_grad_err, 1e-8)
