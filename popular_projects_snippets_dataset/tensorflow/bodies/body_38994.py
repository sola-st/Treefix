# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_add_op_test.py
np.random.seed(1618)  # Make it reproducible.
with self.session(use_gpu=False):
    for n in [10, 31]:
        for m in [4, 17]:
            sp_a, nnz_a = self._randomTensor([n, m], np.float32)
            sp_b, nnz_b = self._randomTensor([n, m], np.float32)
            sp_sum = sparse_ops.sparse_add(sp_a, sp_b)
            nnz_sum = len(self.evaluate(sp_sum.values))

            err = gradient_checker.compute_gradient_error(
                [sp_a.values, sp_b.values], [(nnz_a,), (nnz_b,)], sp_sum.values,
                (nnz_sum,))
            self.assertLess(err, 1e-3)
