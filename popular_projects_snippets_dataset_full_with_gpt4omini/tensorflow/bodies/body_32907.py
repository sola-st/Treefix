# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
for shapes in [[(5, 6), (6, 1)], [(5, 6), (6, 2)]]:
    a_indices = np.array([[0, 0], [2, 3]])
    a_values = np.array([1.0, 5.0]).astype(np.float32)
    a_dense_shape = shapes[0]
    a_sparse_mat = sparse.coo_matrix(
        (a_values, (a_indices[:, 0], a_indices[:, 1])), shape=a_dense_shape)
    a_dense = a_sparse_mat.todense()

    # Will multiply sparse a (shape=shapes[0]) by dense b (shape=shapes[1]).
    b = np.random.randn(*shapes[1]).astype(np.float32)

    a_sm = dense_to_csr_sparse_matrix(a_dense)
    c = sparse_csr_matrix_ops.sparse_matrix_mat_mul(a=a_sm, b=b)
    c_value = self.evaluate(c)

    expected_c_value = a_sparse_mat.dot(b)
    self.assertAllClose(expected_c_value, c_value)
