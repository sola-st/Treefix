# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_math_ops_test.py
eps = 1e-5
x_list = [np.log([0.5, 0.25, 0.25]), np.log([0.5, 0.5])]
x_row_matrices = [[row] for row in x_list]
y_row_matrices = [
    self._softmax(np.array(row_matrix)).tolist()
    for row_matrix in x_row_matrices
]
y_list = [row_matrix[0] for row_matrix in y_row_matrices]
y_expected_from_numpy = ragged_factory_ops.constant(
    y_list, dtype=dtypes.float32)
y_expected = ragged_factory_ops.constant([[0.5, 0.25, 0.25], [0.5, 0.5]],
                                         dtype=dtypes.float32)
self.assertAllClose(y_expected_from_numpy, y_expected, eps)
x_tf = ragged_factory_ops.constant(x_list, dtype=dtypes.float32)
y_tf = nn_ops.softmax_v2(x_tf)
self.assertAllClose(y_tf, y_expected_from_numpy, eps)
