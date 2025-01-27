# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
sparsify = lambda m: m * (m > 0)
dense_shape = [53, 65, 127]
data_types = [
    dtypes.float32, dtypes.float64, dtypes.complex64, dtypes.complex128
]
for dtype in data_types:
    mats = sparsify(
        (np.random.randn(*dense_shape) +
         1.j * np.random.randn(*dense_shape))).astype(dtype.as_numpy_dtype)
    expected = np.transpose(mats, (0, 2, 1))
    for conjugate in False, True:
        if conjugate:
            expected = np.conj(expected)
        matrices = math_ops.cast(mats, dtype)
        sparse_matrices = dense_to_csr_sparse_matrix(matrices)
        transpose_sparse_matrices = \
            sparse_csr_matrix_ops.sparse_matrix_transpose(
                sparse_matrices, conjugate=conjugate, type=dtype)
        dense_transposed = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
            transpose_sparse_matrices, dtype)
        dense_transposed_values = self.evaluate(dense_transposed)
        self.assertAllClose(expected, dense_transposed_values)
