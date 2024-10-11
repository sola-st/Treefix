# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
a_indices = np.array([[0, 0, 0], [0, 2, 3], [2, 0, 1]])
a_values = [1.0, 5.0, 6.0]
a_dense_shape = [3, 5, 6]
a_sparse_mats = [
    sparse.coo_matrix(([1.0, 5.0], ([0, 2], [0, 3])),
                      shape=a_dense_shape[1:]),
    sparse.coo_matrix(([], ([], [])), shape=a_dense_shape[1:]),
    sparse.coo_matrix(([6.0], ([0], [1])), shape=a_dense_shape[1:])
]
a_csr_mats = [m.tocsr() for m in a_sparse_mats]

# Convert 3D SparseTensor to CSR Matrix
a_st = sparse_tensor.SparseTensor(a_indices, a_values, a_dense_shape)
a_st = math_ops.cast(a_st, dtypes.float32)
a_sm = sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
    a_st.indices, a_st.values, a_st.dense_shape)

# Get row indices and columns for batches.
a_sm_components = [
    sparse_csr_matrix_ops.csr_sparse_matrix_components(
        a_sm, i, type=a_st.dtype) for i in range(3)
]

a_sm_values = self.evaluate(a_sm_components)

for i, (a_sm_val, a_csr_mat) in enumerate(zip(a_sm_values, a_csr_mats)):
    tf_logging.info("Comparing batch %d" % i)
    self.assertAllEqual(a_csr_mat.indptr, a_sm_val.row_ptrs)
    self.assertAllEqual(a_csr_mat.indices, a_sm_val.col_inds)
    self.assertAllClose(a_csr_mat.data, a_sm_val.values)

# Convert CSR batched Matrix to 3D SparseTensor
a_st_rt = sparse_csr_matrix_ops.csr_sparse_matrix_to_sparse_tensor(
    a_sm, type=a_st.dtype)
a_st_rt_value = self.evaluate(a_st_rt)

self.assertAllEqual(a_indices, a_st_rt_value.indices)
self.assertAllClose(a_values, a_st_rt_value.values)
self.assertAllEqual(a_dense_shape, a_st_rt_value.dense_shape)
