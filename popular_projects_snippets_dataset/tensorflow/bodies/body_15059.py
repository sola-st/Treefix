# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
"""Tests for RaggedTensor.shape."""
rt1 = RaggedTensor.from_row_splits(b'a b c d e f g'.split(),
                                   [0, 2, 5, 6, 6, 7])
self.assertEqual(rt1.shape.as_list(), [5, None])

rt2 = RaggedTensor.from_row_splits(
    [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14]],
    [0, 2, 5, 6, 6, 7])
self.assertEqual(rt2.shape.as_list(), [5, None, 2])

rt3 = RaggedTensor.from_row_splits(
    [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]], [0, 2, 2, 3])
self.assertEqual(rt3.shape.as_list(), [3, None, 2, 2])

rt4 = RaggedTensor.from_row_splits(rt3, [0, 1, 3, 3])
self.assertEqual(rt4.shape.as_list(), [3, None, None, 2, 2])

if not context.executing_eagerly():
    rt5 = RaggedTensor.from_row_splits(
        array_ops.placeholder(dtype=dtypes.string), [0, 2, 3, 5])
    self.assertIsNone(rt5.shape.ndims)

    rt6 = RaggedTensor.from_row_splits(
        [1, 2, 3], array_ops.placeholder(dtype=dtypes.int64))
    self.assertEqual(rt6.shape.as_list(), [None, None])
