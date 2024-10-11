# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_op_test.py
x = np.random.rand(10, 10)
x[np.abs(x) < 0.5] = 0  # Make it sparse
y = np.random.randn(10, 20)
x_indices = np.vstack(np.where(x)).astype(np.int64).T
x_values = x[np.where(x)]
x_shape = x.shape

with ops.Graph().as_default():
    x_st = sparse_tensor.SparseTensor(x_indices, x_values, x_shape)
    result = sparse_ops.sparse_tensor_dense_matmul(x_st, y)
    self.assertEqual(result.get_shape(), (10, 20))

    x_shape_unknown = array_ops.placeholder(dtype=dtypes.int64, shape=None)
    x_st_shape_unknown = sparse_tensor.SparseTensor(x_indices, x_values,
                                                    x_shape_unknown)
    result_left_shape_unknown = sparse_ops.sparse_tensor_dense_matmul(
        x_st_shape_unknown, y)
    self.assertEqual(result_left_shape_unknown.get_shape().as_list(),
                     [None, 20])

    x_shape_inconsistent = [10, 15]
    x_st_shape_inconsistent = sparse_tensor.SparseTensor(
        x_indices, x_values, x_shape_inconsistent)
    with self.assertRaisesRegex(ValueError, "Dimensions must be equal"):
        sparse_ops.sparse_tensor_dense_matmul(x_st_shape_inconsistent, y)
