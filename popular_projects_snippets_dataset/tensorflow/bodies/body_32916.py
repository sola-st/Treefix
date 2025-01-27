# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()
a_dense_shape = [65, 127]
b_dense_shape = [53, 127, 67]
data_types = [
    dtypes.float32, dtypes.float64, dtypes.complex64, dtypes.complex128
]
for dtype in data_types:
    # Check both rank-2 and rank-3 tensors.
    a_sm = sparse_csr_matrix_ops.sparse_matrix_zeros(
        a_dense_shape, type=dtype)
    b_sm = sparse_csr_matrix_ops.sparse_matrix_zeros(
        b_dense_shape, type=dtype)
    a_rt = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(a_sm, type=dtype)
    b_rt = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(b_sm, type=dtype)
    a_rt_value, b_rt_value = self.evaluate((a_rt, b_rt))

    self.assertAllEqual(a_rt_value, np.zeros(a_dense_shape))
    self.assertAllEqual(b_rt_value, np.zeros(b_dense_shape))
