# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
np.random.seed(1618)
sp_shapes = [(10, 10, 10), (5, 5), (1618,), (3, 3, 7)]
dense_shapes = [(10, 10, 1), (5, 5), (1,), (1, 7)]

with self.session(use_gpu=False):
    for dtype in [np.float32, np.float64]:
        for sp_shape, dense_shape in zip(sp_shapes, dense_shapes):
            sp_vals_np = np.random.rand(*sp_shape).astype(dtype) + 1
            dense_vals_np = np.random.rand(*dense_shape).astype(dtype) + 1
            sp_t, nnz = _sparsify(sp_vals_np, thresh=1.5)
            dense_t = constant_op.constant(dense_vals_np)

            cmul = sp_t * dense_t
            err = gradient_checker.compute_gradient_error([sp_t.values, dense_t],
                                                          [(nnz,), dense_shape],
                                                          cmul.values, (nnz,))
            self.assertLess(err, 1e-4)

            cdiv = sp_t / dense_t
            err = gradient_checker.compute_gradient_error(sp_t.values, (nnz,),
                                                          cdiv.values, (nnz,))
            self.assertLess(err, 1e-4)
            err = gradient_checker.compute_gradient_error(
                dense_t,
                dense_shape,
                cdiv.values, (nnz,),
                x_init_value=dense_vals_np)
            self.assertLess(err, 2e-4)
