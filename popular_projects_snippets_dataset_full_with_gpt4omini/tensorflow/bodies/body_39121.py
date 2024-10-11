# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests mixed type sparse and dense inputs."""
op = sparse_ops.sparse_cross([
    self._sparse_tensor([[11], [333, 5555]]),
    constant_op.constant([['batch1-FC2-F1', 'batch1-FC2-F2'],
                          ['batch2-FC2-F1', 'batch2-FC2-F2']],
                         dtypes.string),
])
expected_out = self._sparse_tensor(
    [['11_X_batch1-FC2-F1', '11_X_batch1-FC2-F2'], [
        '333_X_batch2-FC2-F1', '333_X_batch2-FC2-F2',
        '5555_X_batch2-FC2-F1', '5555_X_batch2-FC2-F2'
    ]])
with self.cached_session() as sess:
    self._assert_sparse_tensor_equals(expected_out, self.evaluate(op))
