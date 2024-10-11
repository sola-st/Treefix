# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests only dense inputs."""
op = sparse_ops.sparse_cross([
    constant_op.constant([['batch1-FC1-F1', 'batch1-FC1-F2'],
                          ['batch2-FC1-F1', 'batch2-FC1-F2']],
                         dtypes.string),
    constant_op.constant([['batch1-FC2-F1', 'batch1-FC2-F2'],
                          ['batch2-FC2-F1', 'batch2-FC2-F2']],
                         dtypes.string),
])
expected_out = self._sparse_tensor([[
    'batch1-FC1-F1_X_batch1-FC2-F1', 'batch1-FC1-F1_X_batch1-FC2-F2',
    'batch1-FC1-F2_X_batch1-FC2-F1', 'batch1-FC1-F2_X_batch1-FC2-F2'
], [
    'batch2-FC1-F1_X_batch2-FC2-F1', 'batch2-FC1-F1_X_batch2-FC2-F2',
    'batch2-FC1-F2_X_batch2-FC2-F1', 'batch2-FC1-F2_X_batch2-FC2-F2'
]])
with self.cached_session() as sess:
    self._assert_sparse_tensor_equals(expected_out, self.evaluate(op))
