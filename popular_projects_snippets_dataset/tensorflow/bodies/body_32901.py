# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
# Test two sets of conversions to check behavior of the ops in a
# concurrent environment (parallel executions of the ST -> SM ops).

sparsify = lambda m: m * (m > 0)
dense_shape = [53, 65, 127]

mats = [
    sparsify(np.random.randn(*dense_shape)).astype(np.float32)
    for _ in range(2)
]
csr_mats = [list(map(sparse.csr_matrix, mat)) for mat in mats]
mats_t = [ops.convert_to_tensor(mat) for mat in mats]
mats_locs = [array_ops.where(mat_t > 0) for mat_t in mats_t]
sparse_tensors = list()
for mat_t, mat_loc in zip(mats_t, mats_locs):
    sparse_tensors.append(
        sparse_tensor.SparseTensor(mat_loc,
                                   array_ops.gather_nd(mat_t,
                                                       mat_loc), dense_shape))
sparse_matrices = [
    sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
        st.indices, st.values, st.dense_shape) for st in sparse_tensors
]
sm_nnz = [
    sparse_csr_matrix_ops.sparse_matrix_nnz(sm) for sm in sparse_matrices
]

# Get row indices and columns for batches.
sm_components = list()
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

    # Convert CSR batched Matrix to 3D SparseTensor
st_rt = [
    sparse_csr_matrix_ops.csr_sparse_matrix_to_sparse_tensor(
        sm, type=dtypes.float32) for sm in sparse_matrices
]

st_values, st_rt_values = self.evaluate((sparse_tensors, st_rt))

for (st_value, st_rt_value) in zip(st_values, st_rt_values):
    self.assertAllEqual(st_value.indices, st_rt_value.indices)
    self.assertAllClose(st_value.values, st_rt_value.values)
    self.assertAllEqual(dense_shape, st_rt_value.dense_shape)
