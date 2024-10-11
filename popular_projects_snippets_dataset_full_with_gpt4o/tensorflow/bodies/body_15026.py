# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = np.array(b'a b c d e f g'.split())
splits = np.array([0, 2, 5, 6, 6, 7], dtype=np.int64)
splits2 = np.array([0, 3, 5], dtype=np.int64)

# Test construction of a RaggedTensorValue with ragged_rank=1.
rt_value = ragged_tensor_value.RaggedTensorValue(values, splits)
self.assertEqual(rt_value.row_splits.dtype, np.int64)
self.assertEqual(rt_value.shape, (5, None))
self.assertLen(rt_value.nested_row_splits, 1)
self.assertAllEqual(splits, rt_value.row_splits)
self.assertAllEqual(values, rt_value.values)
self.assertAllEqual(splits, rt_value.nested_row_splits[0])
self.assertAllEqual(values, rt_value.flat_values)

# Test construction of a RaggedTensorValue with ragged_rank=2.
rt_value = ragged_tensor_value.RaggedTensorValue(
    values=ragged_tensor_value.RaggedTensorValue(values, splits),
    row_splits=splits2)
self.assertEqual(rt_value.row_splits.dtype, np.int64)
self.assertEqual(rt_value.shape, (2, None, None))
self.assertLen(rt_value.nested_row_splits, 2)
self.assertAllEqual(splits2, rt_value.row_splits)
self.assertAllEqual(splits, rt_value.values.row_splits)
self.assertAllEqual(splits2, rt_value.nested_row_splits[0])
self.assertAllEqual(splits, rt_value.nested_row_splits[1])
self.assertAllEqual(values, rt_value.values.values)
self.assertAllEqual(values, rt_value.flat_values)
