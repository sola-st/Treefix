# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_tensor_dense_matmul_grad_test.py
n, k, m = np.random.randint(1, 10, size=3)
sp_t, nnz = self._randomTensor(
    [n, k],
    values_dtype,
    adjoint=adjoint_a,
    sparse=True,
    indices_dtype=indices_dtype)
dense_t = self._randomTensor([k, m], values_dtype, adjoint=adjoint_b)

matmul = sparse_ops.sparse_tensor_dense_matmul(
    sp_t, dense_t, adjoint_a=adjoint_a, adjoint_b=adjoint_b, name=name)

with self.cached_session():
    dense_t_shape = [m, k] if adjoint_b else [k, m]
    sp_t_val_shape = [nnz]
    delta = 1 / 16. if values_dtype == np.float16 else 1e-3
    tolerance = delta / 2. if values_dtype == np.float16 else 1e-3
    err = gradient_checker.compute_gradient_error(
        [dense_t, sp_t.values], [dense_t_shape, sp_t_val_shape],
        matmul, [n, m],
        delta=delta)
    print("%s gradient err = %s" % (name, err))
    self.assertLess(err, tolerance)
