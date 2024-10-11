# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_cross_op_test.py
"""Tests 3x1x2 permutation with hashed output."""
op = sparse_ops.sparse_cross_hashed(
    [
        self._sparse_tensor(
            [['batch1-FC1-F1', 'batch1-FC1-F2', 'batch1-FC1-F3']]),
        self._sparse_tensor([['batch1-FC2-F1']]),
        self._sparse_tensor([['batch1-FC3-F1', 'batch1-FC3-F2']])
    ],
    num_buckets=1000)
with self.cached_session() as sess:
    out = self.evaluate(op)
    self.assertEqual(6, len(out.values))
    self.assertAllEqual([[0, i] for i in range(6)], out.indices)
    self.assertTrue(all(x < 1000 and x >= 0 for x in out.values))
    all_values_are_different = len(out.values) == len(set(out.values))
    self.assertTrue(all_values_are_different)
