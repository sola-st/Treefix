# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
# Tests that numeric zeros appearing from the sparse-sparse matrix
# multiplication are not pruned from the sparse structural
a_indices = np.array([[0, 0], [0, 2]])
a_values = np.array([2.0, -1.0]).astype(np.float32)
a_dense_shape = [2, 3]
a_sparse_mat = sparse.coo_matrix(
    (a_values, (a_indices[:, 0], a_indices[:, 1])), shape=a_dense_shape)
a_dense = a_sparse_mat.todense()

b_indices = np.array([[0, 1], [2, 1]])
b_values = np.array([3.0, 6.0]).astype(np.float32)
b_dense_shape = [3, 2]
b_sparse_mat = sparse.coo_matrix(
    (b_values, (b_indices[:, 0], b_indices[:, 1])), shape=b_dense_shape)
b_dense = b_sparse_mat.todense()

# Convert to CSRSparseMatrix while removing numeric zeros from the
# structural representation.
a_sm = dense_to_csr_sparse_matrix(a_dense)
b_sm = dense_to_csr_sparse_matrix(b_dense)

# Compute the matmul.
c_sm = sparse_csr_matrix_ops.sparse_matrix_sparse_mat_mul(
    a=a_sm, b=b_sm, type=dtypes.float32)
c_nnz = sparse_csr_matrix_ops.sparse_matrix_nnz(c_sm)
c_nnz_value = self.evaluate(c_nnz)

# Expect that there is a single numeric zero at index (0, 1) if zeros are
# not pruned, since 2.0 * 3.0 + (-1.0) * 6.0 = 0.0.
self.assertAllClose(1, c_nnz_value)
