# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
a_dense_shape = [4, 5, 6]
a_sparse_mats = [
    sparse.coo_matrix(([1.0, 5.0], ([0, 2], [0, 3])),
                      shape=a_dense_shape[1:]),
    sparse.coo_matrix(([], ([], [])), shape=a_dense_shape[1:]),
    sparse.coo_matrix(([6.0], ([0], [1])), shape=a_dense_shape[1:]),
    sparse.coo_matrix(([], ([], [])), shape=a_dense_shape[1:]),
]
a_csr_mats = [m.tocsr() for m in a_sparse_mats]
a_dense = np.asarray([m.todense() for m in a_sparse_mats], dtype=np.float32)

# Convert 3D SparseTensor to CSR Matrix
a_sm = dense_to_csr_sparse_matrix(a_dense)

# Get row indices and columns for batches.
a_sm_components = [
    sparse_csr_matrix_ops.csr_sparse_matrix_components(
        a_sm, i, type=dtypes.float32) for i in range(3)
]

a_sm_values = self.evaluate(a_sm_components)

for i, (a_sm_val, a_csr_mat) in enumerate(zip(a_sm_values, a_csr_mats)):
    tf_logging.info("Comparing batch %d" % i)
    self.assertAllEqual(a_csr_mat.indptr, a_sm_val.row_ptrs)
    self.assertAllEqual(a_csr_mat.indices, a_sm_val.col_inds)
    self.assertAllClose(a_csr_mat.data, a_sm_val.values)

# Convert CSR batched Matrix to 3D SparseTensor
a_rt = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
    a_sm, type=dtypes.float32)
a_rt_value = self.evaluate(a_rt)

self.assertAllEqual(a_dense, a_rt_value)
