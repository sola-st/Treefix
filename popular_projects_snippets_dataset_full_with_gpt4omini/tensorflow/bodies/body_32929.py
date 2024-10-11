# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
dense_matrix = np.array([
    [2, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0],
    [1, 1, 7, 0, 0, 0],
    [0, 0, 0, 4, 0, 0],
    [0, 0, 1, 0, 5, 0],
    [0, 0, 2, 0, 1, 6],
]).astype(np.complex128)

data_types = [
    dtypes.float32, dtypes.float64, dtypes.complex64, dtypes.complex128
]
for dtype in data_types:
    with test_util.force_cpu():
        if dtype.is_complex:
            dense_matrix += 0.5j * np.tril(dense_matrix, -1)

        sparse_matrix = dense_to_csr_sparse_matrix(
            math_ops.cast(dense_matrix, dtype))
        # Obtain the Sparse Cholesky factor using AMD Ordering for reducing
        # fill-in.
        ordering_amd = sparse_csr_matrix_ops.sparse_matrix_ordering_amd(
            sparse_matrix)
        cholesky_sparse_matrices = (
            sparse_csr_matrix_ops.sparse_matrix_sparse_cholesky(
                sparse_matrix, ordering_amd, type=dtype))
        dense_cholesky = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
            cholesky_sparse_matrices, dtype)
        # Compute L * Lh where L is the Sparse Cholesky factor.
        verification = test_util.matmul_without_tf32(
            dense_cholesky, array_ops.transpose(dense_cholesky, conjugate=True))
        verification = twist_matrix(verification, ordering_amd)
        # Assert that input matrix A satisfies A = L * Lh.
        verification_values = self.evaluate(verification)
        full_dense_matrix = (
            dense_matrix +
            np.conjugate(np.transpose(np.tril(dense_matrix, -1))))
        self.assertAllClose(full_dense_matrix, verification_values)
