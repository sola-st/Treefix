# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
np.random.seed(1618)  # Make it reproducible.
n, m = np.random.randint(30, size=2)
for dtype in [np.float32, np.float64, np.int64, np.complex64]:
    for index_dtype in [np.int32, np.int64]:
        rand_vals_np = np.random.randn(n, m).astype(dtype)
        dense_np = np.random.randn(n, m).astype(dtype)

        with test_util.force_cpu():
            sparse, unused_nnz = _sparsify(rand_vals_np, index_dtype=index_dtype)
            s = self.evaluate(
                sparse_ops.sparse_add(sparse, constant_op.constant(dense_np)))
            self.assertAllEqual(dense_np + rand_vals_np, s)
            self.assertTrue(s.dtype == dtype)

            # check commutativity
            s = self.evaluate(
                sparse_ops.sparse_add(constant_op.constant(dense_np), sparse))
            self.assertAllEqual(dense_np + rand_vals_np, s)
            self.assertTrue(s.dtype == dtype)
