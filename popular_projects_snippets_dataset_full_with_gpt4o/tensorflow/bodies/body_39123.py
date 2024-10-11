# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests 3x1x2 permutation."""
op = sparse_ops.sparse_cross([
    self._sparse_tensor(
        [['batch1-FC1-F1', 'batch1-FC1-F2', 'batch1-FC1-F3']]),
    self._sparse_tensor([['batch1-FC2-F1']]),
    self._sparse_tensor([['batch1-FC3-F1', 'batch1-FC3-F2']])
])
expected_out = self._sparse_tensor([[
    'batch1-FC1-F1_X_batch1-FC2-F1_X_batch1-FC3-F1',
    'batch1-FC1-F1_X_batch1-FC2-F1_X_batch1-FC3-F2',
    'batch1-FC1-F2_X_batch1-FC2-F1_X_batch1-FC3-F1',
    'batch1-FC1-F2_X_batch1-FC2-F1_X_batch1-FC3-F2',
    'batch1-FC1-F3_X_batch1-FC2-F1_X_batch1-FC3-F1',
    'batch1-FC1-F3_X_batch1-FC2-F1_X_batch1-FC3-F2'
]])
with self.cached_session() as sess:
    self._assert_sparse_tensor_equals(expected_out, self.evaluate(op))
