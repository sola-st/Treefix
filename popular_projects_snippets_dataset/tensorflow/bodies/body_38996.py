# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
np.random.seed(1618)  # Make it reproducible.
n, m = np.random.randint(30, size=2)
rand_vals_np = np.random.randn(n, m).astype(np.float32)
dense_np = np.random.randn(n, m).astype(np.float32)

with self.session(use_gpu=False):
    sparse, nnz = _sparsify(rand_vals_np)
    dense = constant_op.constant(dense_np, dtype=dtypes.float32)
    s = sparse_ops.sparse_add(sparse, dense)

    err = gradient_checker.compute_gradient_error([sparse.values, dense],
                                                  [(nnz,), (n, m)], s, (n, m))
    self.assertLess(err, 1e-3)
