# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_dispatch_test.py
"""Checks that x and y have the same shape (including ragged shapes)."""
if ragged_tensor.is_ragged(x):
    self.assertTrue(ragged_tensor.is_ragged(y))
    self.assertEqual(x.ragged_rank, y.ragged_rank)
    for (x_splits, y_splits) in zip(x.nested_row_splits, y.nested_row_splits):
        self.assertAllEqual(x_splits, y_splits)
    self.assertAllEqual(
        array_ops.shape(x.flat_values), array_ops.shape(y.flat_values))
else:
    self.assertIsInstance(y, ops.Tensor)
    self.assertAllEqual(array_ops.shape(x), array_ops.shape(y))
