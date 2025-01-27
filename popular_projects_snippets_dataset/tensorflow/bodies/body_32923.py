# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m > 0)
dense_shape = [127, 65]
softmax = sparsify(np.random.randn(*dense_shape))
grad_softmax = sparsify(np.random.randn(*dense_shape))
expected = (
    (grad_softmax - np.sum(grad_softmax * softmax, -1, keepdims=True)) *
    softmax)
data_types = [dtypes.float32, dtypes.float64]
for dtype in data_types:
    softmax_t = math_ops.cast(softmax, dtype)
    grad_softmax_t = math_ops.cast(grad_softmax, dtype)
    softmax_sparse = dense_to_csr_sparse_matrix(softmax_t)
    grad_softmax_sparse = dense_to_csr_sparse_matrix(grad_softmax_t)
    gradients_sparse = sparse_csr_matrix_ops.sparse_matrix_softmax_grad(
        softmax_sparse, grad_softmax_sparse, dtype)
    dense_gradients = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
        gradients_sparse, dtype)
    dense_gradients_values = self.evaluate((dense_gradients))
    self.assertAllClose(expected, dense_gradients_values)
