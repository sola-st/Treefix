# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()

batch_size = 53
rows = 128
cols = 67
dense_shape = [batch_size, rows, cols]
data_types = [
    dtypes.float32, dtypes.float64, dtypes.complex64, dtypes.complex128
]
for dtype in data_types:
    sparse_matrices = sparse_csr_matrix_ops.sparse_matrix_zeros(
        dense_shape, type=dtype)
    zeros_like_sparse_matrices = array_ops.zeros_like(sparse_matrices)
    zeros_like_components = [
        sparse_csr_matrix_ops.csr_sparse_matrix_components(
            zeros_like_sparse_matrices, i, type=dtype)
        for i in range(batch_size)
    ]
    zeros_like_components_values = self.evaluate(zeros_like_components)
    for component in zeros_like_components_values:
        self.assertAllEqual(component.row_ptrs, np.zeros(rows + 1, np.int32))
        self.assertAllEqual(component.col_inds, np.empty([0], np.int32))
        self.assertAllEqual(component.values, np.empty([0],
                                                       dtype.as_numpy_dtype))
