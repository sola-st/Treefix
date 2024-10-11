# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
# Verify that non-SPD matrices result in an Invalid Argument error.
invalid_matrices = [
    # zero matrix.
    np.array([
        [0., 0., 0., 0.],  #
        [0., 0., 0., 0.],  #
        [0., 0., 0., 0.],  #
        [0., 0., 0., 0.]  #
    ]),
    # zero diagonal entry.
    np.array([
        [9., 0., 5., 0.],  #
        [0., 0., 0., 1.],  #
        [5., 0., 8., 0.],  #
        [0., 1., 0., 7.]  #
    ]),
    # not positive definite.
    np.array([
        [2., -2., 0., 0.],  #
        [-2., 2., 0., 0.],  #
        [0., 0., 3., -3.],  #
        [0., 0., -3., 3.]  #
    ]),
]

with test_util.force_cpu():
    for invalid_matrix in invalid_matrices:
        with self.assertRaises(errors.InvalidArgumentError):
            sparse_matrix = dense_to_csr_sparse_matrix(
                invalid_matrix.astype(np.float32))
            # Compute the fill-in reducing permutation and use it to perform
            # the Sparse Cholesky factorization.
            ordering_amd = sparse_csr_matrix_ops.sparse_matrix_ordering_amd(
                sparse_matrix)
            cholesky_sparse_matrices = (
                sparse_csr_matrix_ops.sparse_matrix_sparse_cholesky(
                    sparse_matrix, ordering_amd, type=dtypes.float32))
            # Convert the Cholesky factor to a dense matrix to be evaluated.
            dense_cholesky = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
                cholesky_sparse_matrices, type=dtypes.float32)
            self.evaluate(dense_cholesky)
