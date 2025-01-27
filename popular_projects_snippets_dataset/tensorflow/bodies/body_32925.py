# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m > 0)
dense_shape = [53, 65, 127]
not_empty = sparsify(np.random.randn(*dense_shape)).astype(np.float32)
sparse_empty = sparse_csr_matrix_ops.sparse_matrix_zeros(
    dense_shape, type=dtypes.float32)
sparse_not_empty = dense_to_csr_sparse_matrix(not_empty)
gradients_empty_softmax = sparse_csr_matrix_ops.sparse_matrix_softmax_grad(
    sparse_empty, sparse_not_empty, dtypes.float32)
gradients_empty_grad_softmax = (
    sparse_csr_matrix_ops.sparse_matrix_softmax_grad(
        sparse_not_empty, sparse_empty, dtypes.float32))
gradients_empty_both = sparse_csr_matrix_ops.sparse_matrix_softmax_grad(
    sparse_empty, sparse_empty, dtypes.float32)
ges = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
    gradients_empty_softmax, dtypes.float32)
gegs = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
    gradients_empty_grad_softmax, dtypes.float32)
geb = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
    gradients_empty_both, dtypes.float32)
ges_v, gegs_v, geb_v = self.evaluate((ges, gegs, geb))
for v in (ges_v, gegs_v, geb_v):
    self.assertAllEqual(np.zeros(dense_shape), v)
