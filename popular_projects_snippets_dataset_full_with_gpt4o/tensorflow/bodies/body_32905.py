# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()

a_indices = np.array([[0, 0], [2, 3]])
a_values = np.array([1.0, 5.0]).astype(np.float32)
a_dense_shape = [5, 6]
a_sparse_mat = sparse.coo_matrix(
    (a_values, (a_indices[:, 0], a_indices[:, 1])), shape=a_dense_shape)
a_dense = a_sparse_mat.todense()

b_indices = np.array([[1, 0], [1, 4], [2, 3], [4, 1]])
b_values = np.array([1.0, 0.5, -5.0, 2.0]).astype(np.float32)
b_dense_shape = [5, 6]
b_sparse_mat = sparse.coo_matrix(
    (b_values, (b_indices[:, 0], b_indices[:, 1])), shape=b_dense_shape)
b_dense = b_sparse_mat.todense()

for (alpha, beta) in [(1.0, 1.0), (1.0, -1.0), (0.25, 0.5)]:
    a_sum_b_sparse_mat = alpha * a_sparse_mat + beta * b_sparse_mat

    # Convert 2D SparseTensor to CSR Matrix
    a_sm = dense_to_csr_sparse_matrix(a_dense)
    b_sm = dense_to_csr_sparse_matrix(b_dense)
    alpha = np.float32(alpha)
    beta = np.float32(beta)
    c_sm = sparse_csr_matrix_ops.sparse_matrix_add(
        a_sm, b_sm, alpha=alpha, beta=beta)
    c_dense = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
        c_sm, dtypes.float32)
    c_dense_value = self.evaluate(c_dense)

    self.assertAllClose(a_sum_b_sparse_mat.todense(), c_dense_value)
