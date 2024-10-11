# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests when one column is empty.

    The crossed tensor should be empty.
    """
op = sparse_ops.sparse_cross([
    self._sparse_tensor([['batch1-FC1-F1', 'batch1-FC1-F2']]),
    self._sparse_tensor([], 1),
    self._sparse_tensor([['batch1-FC3-F1', 'batch1-FC3-F2']])
])
with self.cached_session() as sess:
    self._assert_sparse_tensor_empty(self.evaluate(op))
