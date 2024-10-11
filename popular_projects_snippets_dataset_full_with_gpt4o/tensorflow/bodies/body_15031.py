# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
value_rowids = constant_op.constant([0, 0, 2, 2, 2, 3, 4], dtypes.int64)
nrows = constant_op.constant(7, dtypes.int64)

rt = RaggedTensor.from_value_rowids(
    values, value_rowids, nrows, validate=False)
self.assertEqual(rt.dtype, dtypes.string)
self.assertEqual(rt.shape.as_list(), [7, None])
self.assertEqual(rt.ragged_rank, 1)

rt_values = rt.values
rt_value_rowids = rt.value_rowids()
rt_nrows = rt.nrows()

self.assertIs(rt_values, values)
self.assertIs(rt_value_rowids, value_rowids)  # cached_value_rowids
self.assertIs(rt_nrows, nrows)  # cached_nrows
self.assertAllEqual(
    rt, [[b'a', b'b'], [], [b'c', b'd', b'e'], [b'f'], [b'g'], [], []])
