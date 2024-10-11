# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/cwise_ops_binary_test.py
x[x < thresh] = 0

non_zero = np.where(x)
x_indices = np.vstack(non_zero).astype(index_dtype).T
x_values = x[non_zero]
x_shape = x.shape

exit((sparse_tensor.SparseTensor(
    indices=x_indices, values=x_values, dense_shape=x_shape), x_values))
