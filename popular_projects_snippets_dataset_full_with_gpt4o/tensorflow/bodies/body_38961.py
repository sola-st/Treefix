# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
if np.__version__ == "1.13.0":
    self.skipTest("numpy 1.13.0 bug")

sp_t = sparse_tensor.SparseTensor(self.ind, self.vals, self.dense_shape)

with test_util.force_cpu():
    self._compare_all(sp_t, None, ndims=2)
    self._compare_all(sp_t, 0, ndims=2)
    self._compare_all(sp_t, [1], ndims=2)
    self._compare_all(sp_t, [0, 1], ndims=2)
    self._compare_all(sp_t, [1, 0], ndims=2)
    self._compare_all(sp_t, [-1], ndims=2)
    self._compare_all(sp_t, [1, -2], ndims=2)

np.random.seed(1618)
test_dims = [(1618, 1, 11, 7, 1), (1,), (1, 1, 1)]
with test_util.force_cpu():
    for dims in test_dims:
        sp_t, unused_nnz = _sparsify(np.random.randn(*dims))
        # reduce all using None
        self._compare_all(sp_t, None, ndims=len(dims))
        # reduce random axes from 1D to N-D
        for d in range(1, len(dims) + 1):
            axes = np.random.choice(len(dims), size=d, replace=False).tolist()
            self._compare_all(sp_t, axes, ndims=len(dims))
