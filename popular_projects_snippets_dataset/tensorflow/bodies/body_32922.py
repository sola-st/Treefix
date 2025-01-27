# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()

dense_shape = [53, 65, 127]
sparse_logits_t = sparse_csr_matrix_ops.sparse_matrix_zeros(
    dense_shape, type=dtypes.float32)
softmax_sparse_logits_t = sparse_csr_matrix_ops.sparse_matrix_softmax(
    sparse_logits_t, type=dtypes.float32)
dense_softmax = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
    softmax_sparse_logits_t, dtypes.float32)
dense_softmax_values = self.evaluate(dense_softmax)
self.assertAllEqual(
    np.zeros_like(dense_softmax_values), dense_softmax_values)
