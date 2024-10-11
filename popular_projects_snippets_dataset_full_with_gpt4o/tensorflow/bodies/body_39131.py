# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
op = sparse_ops.sparse_cross_hashed(
    [
        self._sparse_tensor([['batch1-FC1-F1']]),
        self._sparse_tensor([['batch1-FC2-F1']]),
        self._sparse_tensor([['batch1-FC3-F1']])
    ],
    num_buckets=100,
    hash_key=sparse_ops._DEFAULT_HASH_KEY + 1)
# Check actual hashed output to prevent unintentional hashing changes.
expected_out = self._sparse_tensor([[31]])
with self.cached_session() as sess:
    self._assert_sparse_tensor_equals(expected_out, self.evaluate(op))
