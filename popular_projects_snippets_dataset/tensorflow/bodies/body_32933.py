# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
num_rows = 6
# An SPD matrix where AMD ordering can reduce fill-in for Cholesky factor.
dense_matrix = np.array([
    [7, 0, 0, 0, 0, 0],
    [1, 4, 0, 0, 0, 0],
    [1, 1, 3, 0, 0, 0],
    [0, 0, 0, 4, 0, 0],
    [2, 0, 0, 0, 5, 0],
    [1, 2, 2, 0, 0, 6],
]).astype(np.float32)

with test_util.force_cpu():
    sparse_matrix = dense_to_csr_sparse_matrix(dense_matrix)

    # Obtain the Sparse Cholesky factor with the identity permutation as the
    # fill-in reducing ordering.
    cholesky_without_ordering = (
        sparse_csr_matrix_ops.sparse_matrix_sparse_cholesky(
            sparse_matrix, math_ops.range(num_rows), type=dtypes.float32))
    cholesky_without_ordering_nnz = sparse_csr_matrix_ops.sparse_matrix_nnz(
        cholesky_without_ordering)

    # Obtain the Sparse Cholesky factor using AMD Ordering for reducing
    # fill-in.
    ordering_amd = sparse_csr_matrix_ops.sparse_matrix_ordering_amd(
        sparse_matrix)
    cholesky_with_amd = sparse_csr_matrix_ops.sparse_matrix_sparse_cholesky(
        sparse_matrix, ordering_amd, type=dtypes.float32)
    cholesky_with_amd_nnz = sparse_csr_matrix_ops.sparse_matrix_nnz(
        cholesky_with_amd)

    (ordering_amd_value, cholesky_with_amd_nnz_value,
     cholesky_without_ordering_nnz_value) = self.evaluate(
         [ordering_amd, cholesky_with_amd_nnz, cholesky_without_ordering_nnz])

    # AMD ordering should return a valid permutation.
    self.assertAllClose(np.arange(num_rows), np.sort(ordering_amd_value))
    # Check that cholesky with AMD ordering has a strictly lower nonzero count
    # for this matrix.
    self.assertLess(cholesky_with_amd_nnz_value,
                    cholesky_without_ordering_nnz_value)
