# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
np.random.seed(1618)
sp_shapes = [(10, 10, 10), (5, 5), (1618,), (3, 3, 7)]
dense_shapes = [(10, 10, 1), (5, 5), (1,), (1, 7)]

with test_util.force_cpu():
    for dtype in [np.float32, np.float64, np.int32, np.int64]:
        for sp_shape, dense_shape in zip(sp_shapes, dense_shapes):
            sp_vals_np = np.random.rand(*sp_shape).astype(dtype) + 1
            dense_vals_np = np.random.rand(*dense_shape).astype(dtype) + 1
            sp_t, unused_nnz = _sparsify(sp_vals_np, thresh=1.5)
            sp_t_densified = sparse_ops.sparse_tensor_to_dense(sp_t)
            dense_t = constant_op.constant(dense_vals_np)

            self._check(sp_t / dense_t, sp_t_densified / dense_vals_np, sp_t)
            # Check commutative.
            self._check(sp_t * dense_t, sp_t_densified * dense_vals_np, sp_t)
            self._check(dense_t * sp_t, sp_t_densified * dense_vals_np, sp_t)

            if dtype in [np.int32, np.int64]:
                res = sp_t / dense_t  # should invoke "__truediv__"
                self.assertEqual(res.values.dtype, np.float64)
