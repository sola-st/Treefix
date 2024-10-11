# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_grad_test.py
sparsify = lambda m: m * (m > 0)
for dense_shape in ([53, 65, 127], [127, 65]):
    mats_val = sparsify(np.random.randn(*dense_shape))

    with self.session(use_gpu=True) as sess:
        indices = array_ops.where_v2(
            math_ops.not_equal(mats_val, array_ops.zeros_like(mats_val)))
        values = math_ops.cast(
            array_ops.gather_nd(mats_val, indices), dtype=dtypes.float32)

        grad_vals = np.random.randn(*sess.run(values).shape).astype(np.float32)
        csr_matrix = sparse_csr_matrix_ops.sparse_tensor_to_csr_sparse_matrix(
            indices, values, dense_shape)
        new_coo_tensor = (
            sparse_csr_matrix_ops.csr_sparse_matrix_to_sparse_tensor(
                csr_matrix, type=dtypes.float32))
        grad_out = gradients_impl.gradients([new_coo_tensor.values], [values],
                                            [grad_vals])[0]
        self.assertEqual(grad_out.dtype, dtypes.float32)
        grad_out_vals = sess.run(grad_out)
        self.assertAllClose(grad_vals, grad_out_vals)
