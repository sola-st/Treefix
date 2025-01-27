# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
dense_mat = np.array([
    # A diagonal matrix.
    [
        [1, 0, 0, 0],  #
        [0, 2, 0, 0],  #
        [0, 0, 3, 0],  #
        [0, 0, 0, 4],
    ],  #
    # A tridiagonal hermitian matrix.
    [
        [5 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],  #
        [1 + 0j, 4 + 0j, 1 + 2j, 0 + 0j],  #
        [0 + 0j, 1 - 2j, 9 + 0j, 3 - 3j],  #
        [0 + 0j, 0 + 0j, 3 + 3j, 7 + 0j],
    ],  #
    # A diagonal matrix with a corner element; for which
    # OrderingAMD returns a non-identity permutation.
    [
        [1, 0, 0, 1.],  #
        [0, 2, 0, 0.],  #
        [0, 0, 3, 0.],  #
        [1, 0, 0, 4.],
    ]  #
]).astype(np.complex128)

data_types = [
    dtypes.float32, dtypes.float64, dtypes.complex64, dtypes.complex128
]
for dtype in data_types:
    sparse_matrix = dense_to_csr_sparse_matrix(
        math_ops.cast(dense_mat, dtype))
    ordering_amd = sparse_csr_matrix_ops.sparse_matrix_ordering_amd(
        sparse_matrix)

    cholesky_sparse_matrix = (
        sparse_csr_matrix_ops.sparse_matrix_sparse_cholesky(
            sparse_matrix, ordering_amd, type=dtype))
    dense_cholesky = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
        cholesky_sparse_matrix, dtype)

    # Compute L * Lh.
    verification = test_util.matmul_without_tf32(
        dense_cholesky,
        array_ops.transpose(dense_cholesky, perm=[0, 2, 1], conjugate=True))
    verification = twist_matrix(verification, ordering_amd)

    verification_values = self.evaluate(verification)
    self.assertAllClose(
        dense_mat.astype(dtype.as_numpy_dtype), verification_values)
