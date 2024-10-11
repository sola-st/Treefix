# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_grad_test.py
if not self._gpu_available:
    exit()

sparsify = lambda m: m * (m > 0)
for dense_shape in ([53, 65, 127], [127, 65]):
    mats_val = sparsify(np.random.randn(*dense_shape))
    with self.test_session() as sess:
        mats = math_ops.cast(mats_val, dtype=dtypes.float32)
        sparse_mats = dense_to_csr_sparse_matrix(mats)
        dense_mats = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
            sparse_mats, dtypes.float32)
        grad_vals = np.random.randn(*dense_shape).astype(np.float32)
        grad_out = gradients_impl.gradients([dense_mats], [mats],
                                            [grad_vals])[0]
        self.assertEqual(grad_out.dtype, dtypes.float32)
        self.assertEqual(grad_out.shape, dense_shape)
        grad_out_value = sess.run(grad_out)
        tf_logging.info("testLargeBatchConversionGrad: Testing shape %s" %
                        dense_shape)
        nonzero_indices = abs(mats_val) > 0.0
        self.assertAllEqual(grad_out_value[nonzero_indices],
                            grad_vals[nonzero_indices])
        self.assertTrue(
            np.all(grad_out_value[np.logical_not(nonzero_indices)] == 0.0))
