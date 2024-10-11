# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m > 0)
dense_shape = [53, 65, 127]
logits = sparsify(np.random.randn(*dense_shape))
logits_with_ninf = np.copy(logits)
logits_with_ninf[logits == 0] = -np.inf
data_types = [dtypes.float32, dtypes.float64]
for dtype in data_types:
    logits_t = math_ops.cast(logits, dtype)
    logits_t_with_ninf = math_ops.cast(logits_with_ninf, dtype)
    expected = nn_ops.softmax(logits_t_with_ninf)
    sparse_logits_t = dense_to_csr_sparse_matrix(logits_t)
    softmax_sparse_logits_t = sparse_csr_matrix_ops.sparse_matrix_softmax(
        sparse_logits_t, type=dtype)
    dense_softmax = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
        softmax_sparse_logits_t, dtype)
    dense_softmax_values, expected_values = self.evaluate(
        (dense_softmax, expected))
    self.assertAllClose(expected_values, dense_softmax_values)
