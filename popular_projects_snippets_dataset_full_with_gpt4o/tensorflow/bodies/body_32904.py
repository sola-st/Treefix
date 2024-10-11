# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
# Test two sets of conversions to check behavior of the ops in a
# concurrent environment (parallel executions of the ST -> SM
# ops).

sparsify = lambda m: m * (m > 0)
dense_shape = [53, 65, 127]

mats = [
    sparsify(np.random.randn(*dense_shape)).astype(np.float32)
    for _ in range(2)
]
csr_mats = [[sparse.csr_matrix(m) for m in mat] for mat in mats]
mats_t = [ops.convert_to_tensor(mat) for mat in mats]
mats_locs = [array_ops.where(mat_t > 0) for mat_t in mats_t]
sparse_matrices = [
    sparse_csr_matrix_ops.dense_to_csr_sparse_matrix(mat, mat_loc)
    for (mat, mat_loc) in zip(mats_t, mats_locs)
]
sm_nnz = [
    sparse_csr_matrix_ops.sparse_matrix_nnz(sm) for sm in sparse_matrices
]

# Get row indices and columns for batches.
sm_components = []
for sm in sparse_matrices:
    sm_components.append([
        sparse_csr_matrix_ops.csr_sparse_matrix_components(
            sm, i, type=dtypes.float32) for i in range(dense_shape[0])
    ])

sm_nnz_values, sm_values = self.evaluate((sm_nnz, sm_components))

for i, (sm_values_i, csr_mats_i) in enumerate(zip(sm_values, csr_mats)):
    for b, (sm_val, csr_mat) in enumerate(zip(sm_values_i, csr_mats_i)):
        tf_logging.info("Comparing matrix %d batch %d" % (i, b))
        self.assertEqual(csr_mat.nnz, sm_nnz_values[i][b])
        self.assertAllEqual(csr_mat.indptr, sm_val.row_ptrs)
        self.assertAllEqual(csr_mat.indices, sm_val.col_inds)
        self.assertAllClose(csr_mat.data, sm_val.values)

    # Convert CSR batched Matrix to 3D dense tensor
sm_rt = [
    sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
        sm, type=dtypes.float32) for sm in sparse_matrices
]

sm_rt_values = self.evaluate(sm_rt)

for (mat, sm_rt_value) in zip(mats, sm_rt_values):
    self.assertAllEqual(mat, sm_rt_value)
