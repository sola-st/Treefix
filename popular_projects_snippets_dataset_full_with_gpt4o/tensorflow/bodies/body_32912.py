# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
a_indices = np.array([[0, 0], [2, 3]])
a_values = np.array([1.0, 5.0]).astype(np.float32)
a_dense_shape = [5, 6]
a_sparse_mat = sparse.coo_matrix(
    (a_values, (a_indices[:, 0], a_indices[:, 1])), shape=a_dense_shape)
a_dense = a_sparse_mat.todense()

b_indices = np.array([[0, 0], [3, 0], [3, 1]])
b_values = np.array([2.0, 7.0, 8.0]).astype(np.float32)
b_dense_shape = [6, 7]
b_sparse_mat = sparse.coo_matrix(
    (b_values, (b_indices[:, 0], b_indices[:, 1])), shape=b_dense_shape)
b_dense = b_sparse_mat.todense()

a_sm = dense_to_csr_sparse_matrix(a_dense)
b_sm = dense_to_csr_sparse_matrix(b_dense)
c_sm = sparse_csr_matrix_ops.sparse_matrix_sparse_mat_mul(
    a=a_sm, b=b_sm, type=dtypes.float32)

c_sm_dense = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
    c_sm, dtypes.float32)
c_sm_dense_value = self.evaluate(c_sm_dense)

expected_c_value = a_sparse_mat.dot(b_sparse_mat).todense()
self.assertAllClose(expected_c_value, c_sm_dense_value)
