# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
nested_value_rowids = [
    constant_op.constant([0, 0, 1, 3, 3], dtypes.int64),
    constant_op.constant([0, 0, 2, 2, 2, 3, 4], dtypes.int64)
]

rt = RaggedTensor.from_nested_value_rowids(values, nested_value_rowids)
self.assertEqual(rt.dtype, dtypes.string)
self.assertEqual(rt.shape.as_list(), [4, None, None])
self.assertEqual(rt.ragged_rank, 2)

rt_values = rt.values
rt_value_rowids = rt.value_rowids()
rt_values_values = rt_values.values
rt_values_value_rowids = rt_values.value_rowids()

self.assertIs(rt_values_values, values)
self.assertAllEqual(rt_value_rowids, nested_value_rowids[0])
self.assertAllEqual(rt_values_value_rowids, nested_value_rowids[1])
self.assertAllEqual(
    rt, [[[b'a', b'b'], []], [[b'c', b'd', b'e']], [], [[b'f'], [b'g']]])
