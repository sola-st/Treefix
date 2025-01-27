# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m > 0)
dense_shape = [53, 65, 127]
a_mats = sparsify(np.random.randn(*dense_shape)).astype(np.float32)
b_mats = sparsify(np.random.randn(*dense_shape)).astype(np.float32)
for (alpha, beta) in [(1.0, 1.0), (1.0, -1.0), (0.25, 0.5)]:
    tf_logging.info("testLargeBatchSparseMatrixAdd, comparing "
                    "alpha, beta (%d, %d)" % (alpha, beta))
    a_sm = dense_to_csr_sparse_matrix(a_mats)
    b_sm = dense_to_csr_sparse_matrix(b_mats)
    alpha = np.float32(alpha)
    beta = np.float32(beta)
    c_sm = sparse_csr_matrix_ops.sparse_matrix_add(
        a_sm, b_sm, alpha=alpha, beta=beta)
    c_dense = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
        c_sm, dtypes.float32)
    c_dense_value = self.evaluate(c_dense)

    self.assertAllClose(c_dense_value, alpha * a_mats + beta * b_mats)
