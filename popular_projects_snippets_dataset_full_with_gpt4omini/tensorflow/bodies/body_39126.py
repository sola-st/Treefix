# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests when more than one columns are empty.

    Cross for the corresponding batch should be empty.
    """
op = sparse_ops.sparse_cross([
    self._sparse_tensor([['batch1-FC1-F1', 'batch1-FC1-F2']], 2),
    self._sparse_tensor([['batch1-FC2-F1'], ['batch2-FC2-F1']], 2),
    self._sparse_tensor([['batch1-FC3-F1', 'batch1-FC3-F2']], 2)
])
expected_out = self._sparse_tensor([[
    'batch1-FC1-F1_X_batch1-FC2-F1_X_batch1-FC3-F1',
    'batch1-FC1-F1_X_batch1-FC2-F1_X_batch1-FC3-F2',
    'batch1-FC1-F2_X_batch1-FC2-F1_X_batch1-FC3-F1',
    'batch1-FC1-F2_X_batch1-FC2-F1_X_batch1-FC3-F2'
]], 2)
with self.cached_session() as sess:
    self._assert_sparse_tensor_equals(expected_out, self.evaluate(op))
