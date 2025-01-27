# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
a_indices = np.array([[0, 0], [2, 3], [2, 4], [3, 0]])
a_values = [1.0, 5.0, -1.0, -2.0]
a_dense_shape = [5, 6]
a_sparse_mat = sparse.coo_matrix(
    (a_values, (a_indices[:, 0], a_indices[:, 1])), shape=a_dense_shape)
a_csr_mat = a_sparse_mat.tocsr()

# Convert 2D SparseTensor to CSR Matrix
a_st = sparse_tensor.SparseTensor(a_indices, a_values, a_dense_shape)
a_st = math_ops.cast(a_st, dtypes.float32)
a_sm = sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
    a_st.indices, a_st.values, a_st.dense_shape)

# Get row indices and columns for batch 0.
a_sm_row_ptrs, a_sm_col_inds, a_sm_values = (
    sparse_csr_matrix_ops.csr_sparse_matrix_components(
        a_sm, 0, type=a_st.dtype))

a_sm_row_ptrs_values, a_sm_col_inds_values, a_sm_values_values = (
    self.evaluate((a_sm_row_ptrs, a_sm_col_inds, a_sm_values)))

self.assertAllEqual(a_csr_mat.indices, a_sm_col_inds_values)
self.assertAllEqual(a_csr_mat.indptr, a_sm_row_ptrs_values)
self.assertAllClose(a_values, a_sm_values_values)

# Convert CSR Matrix to 2D SparseTensor
a_st_rt = sparse_csr_matrix_ops.csr_sparse_matrix_to_sparse_tensor(
    a_sm, type=a_st.dtype)
a_st_rt_value = self.evaluate(a_st_rt)

self.assertAllEqual(a_indices, a_st_rt_value.indices)
self.assertAllClose(a_values, a_st_rt_value.values)
self.assertAllEqual(a_dense_shape, a_st_rt_value.dense_shape)
