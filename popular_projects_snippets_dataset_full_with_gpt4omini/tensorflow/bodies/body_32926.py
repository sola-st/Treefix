# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (np.real(m) > 0)
dense_shape = [53, 65, 127]
matrices = (
    sparsify(np.random.randn(*dense_shape)) +
    1j * np.random.randn(*dense_shape))
data_types = [
    dtypes.float32, dtypes.float64, dtypes.complex64, dtypes.complex128
]
for dtype in data_types:
    matrices_t = matrices.astype(dtype.as_numpy_dtype)
    expected = np.conj(matrices_t)
    sparse_matrices = dense_to_csr_sparse_matrix(matrices_t)
    conj_sparse_matrices = math_ops.conj(sparse_matrices)
    dense_conj_matrices = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
        conj_sparse_matrices, dtype)
    conj_values = self.evaluate(dense_conj_matrices)
    self.assertAllClose(expected, conj_values)
