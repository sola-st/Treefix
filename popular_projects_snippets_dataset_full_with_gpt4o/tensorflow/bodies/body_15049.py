# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
flat_values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
nested_row_splits = [
    constant_op.constant([0, 2, 3, 3, 5], dtypes.int64),
    constant_op.constant([0, 2, 2, 5, 6, 7], dtypes.int64)
]

rt = RaggedTensor.from_nested_row_splits(
    flat_values, nested_row_splits, validate=False)
self.assertEqual(rt.dtype, dtypes.string)
self.assertEqual(rt.shape.as_list(), [4, None, None])
self.assertEqual(rt.ragged_rank, 2)

rt_values = rt.values
rt_row_splits = rt.row_splits
rt_values_values = rt_values.values
rt_values_row_splits = rt_values.row_splits

self.assertIs(rt_values_values, flat_values)
self.assertIs(rt_row_splits, nested_row_splits[0])
self.assertIs(rt_values_row_splits, nested_row_splits[1])
self.assertAllEqual(
    rt, [[[b'a', b'b'], []], [[b'c', b'd', b'e']], [], [[b'f'], [b'g']]])
