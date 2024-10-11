# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
np.random.seed(8161)
test_dims = [(11, 1, 5, 7, 1), (2, 2)]
with self.session(use_gpu=False):
    for dims in test_dims:
        sp_t, nnz = _sparsify(np.random.randn(*dims))
        # reduce random axes from 1D to N-D
        for d in range(1, len(dims) + 1):
            axes = np.random.choice(len(dims), size=d, replace=False).tolist()
            reduced = sparse_ops.sparse_reduce_sum(sp_t, axes)

            err = gradient_checker.compute_gradient_error(
                sp_t.values, (nnz,), reduced,
                self.evaluate(reduced).shape)
            self.assertLess(err, 1e-3)

        # Tests for negative axes.
        reduced = sparse_ops.sparse_reduce_sum(sp_t, -1)
        err = gradient_checker.compute_gradient_error(
            sp_t.values, (nnz,), reduced,
            self.evaluate(reduced).shape)
        self.assertLess(err, 1e-3)
