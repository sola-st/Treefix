# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_grad_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m > 0)
for dense_shape in ([53, 65, 127], [127, 65]):
    a_mats_val = sparsify(np.random.randn(*dense_shape))
    b_mats_val = sparsify(np.random.randn(*dense_shape))
    alpha = np.float32(0.5)
    beta = np.float32(-1.5)
    grad_vals = np.random.randn(*dense_shape).astype(np.float32)
    expected_a_grad = alpha * grad_vals
    expected_b_grad = beta * grad_vals
    expected_a_grad[abs(a_mats_val) == 0.0] = 0.0
    expected_b_grad[abs(b_mats_val) == 0.0] = 0.0
    with self.test_session() as sess:
        a_mats = math_ops.cast(a_mats_val, dtype=dtypes.float32)
        b_mats = math_ops.cast(b_mats_val, dtype=dtypes.float32)
        a_sm = dense_to_csr_sparse_matrix(a_mats)
        b_sm = dense_to_csr_sparse_matrix(b_mats)
        c_sm = sparse_csr_matrix_ops.sparse_matrix_add(
            a_sm, b_sm, alpha=alpha, beta=beta)
        c_dense = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
            c_sm, dtypes.float32)
        a_grad, b_grad = gradients_impl.gradients([c_dense], [a_mats, b_mats],
                                                  [grad_vals])
        self.assertEqual(a_grad.dtype, dtypes.float32)
        self.assertEqual(b_grad.dtype, dtypes.float32)
        self.assertEqual(a_grad.shape, dense_shape)
        self.assertEqual(b_grad.shape, dense_shape)
        a_grad_value, b_grad_value = sess.run((a_grad, b_grad))
        tf_logging.info("testLargeBatchConversionGrad: Testing shape %s" %
                        dense_shape)
        self.assertAllEqual(expected_a_grad, a_grad_value)
        self.assertAllEqual(expected_b_grad, b_grad_value)
