# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
sp_t = sparse_tensor.SparseTensor(self.ind, self.vals, self.dense_shape)

with test_util.force_cpu():
    for do_sum in [True, False]:
        for keep_dims in [True, False]:
            self._testSparseReduceShape(sp_t, None, 2, keep_dims, do_sum)
            self._testSparseReduceShape(sp_t, 0, 2, keep_dims, do_sum)
            self._testSparseReduceShape(sp_t, [1], 2, keep_dims, do_sum)
            self._testSparseReduceShape(sp_t, [0, 1], 2, keep_dims, do_sum)
            self._testSparseReduceShape(sp_t, [1, 0], 2, keep_dims, do_sum)
            self._testSparseReduceShape(sp_t, [-1], 2, keep_dims, do_sum)
            self._testSparseReduceShape(sp_t, [1, -2], 2, keep_dims, do_sum)
