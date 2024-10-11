# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests when all columns are empty.

    The crossed tensor should be empty.
    """
op = sparse_ops.sparse_cross([
    self._sparse_tensor([]),
    self._sparse_tensor([]),
    self._sparse_tensor([])
])
with self.cached_session() as sess:
    self._assert_sparse_tensor_empty(self.evaluate(op))
