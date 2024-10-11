# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_grad_test.py
x[x < 0.5] = 0

non_zero = np.where(x)
x_indices = np.vstack(non_zero).astype(indices_dtype).T
x_values = x[non_zero]
x_shape = x.shape

exit((sparse_tensor.SparseTensor(
    indices=x_indices, values=x_values, dense_shape=x_shape), len(x_values)))
