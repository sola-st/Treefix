# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_ops_test.py
sp_t = sparse_tensor.SparseTensor(self.ind, self.vals, self.dense_shape)
with test_util.force_cpu():
    with self.assertRaisesOpError("Invalid reduction dimension -3"):
        self.evaluate(sparse_ops.sparse_reduce_sum(sp_t, -3))
    with self.assertRaisesOpError("Invalid reduction dimension 2"):
        self.evaluate(sparse_ops.sparse_reduce_sum(sp_t, 2))
    with self.assertRaisesOpError("Invalid reduction dimension -3"):
        self.evaluate(sparse_ops.sparse_reduce_max(sp_t, -3))
    with self.assertRaisesOpError("Invalid reduction dimension 2"):
        self.evaluate(sparse_ops.sparse_reduce_max(sp_t, 2))
