# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m > 0)
dense_shape = [53, 65, 127]
matrices = [
    sparsify(np.random.randn(*dense_shape)).astype(np.float32)
    for _ in range(16)
]
sparse_matrices = [dense_to_csr_sparse_matrix(mat) for mat in matrices]
sparse_matrices_sum = math_ops.add_n(sparse_matrices)
sparse_matrices_sum_dense = \
        sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
        sparse_matrices_sum, dtypes.float32)
sparse_matrices_sum_dense_value = self.evaluate(sparse_matrices_sum_dense)

# Ensure that the dense (numpy) sum across all batches matches the result
# of add_n converted back to dense.
expected_sum = np.sum(matrices, axis=0)
self.assertAllClose(expected_sum, sparse_matrices_sum_dense_value)
