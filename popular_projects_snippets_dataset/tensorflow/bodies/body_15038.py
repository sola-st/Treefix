# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
row_limits = constant_op.constant([2, 2, 5, 6, 7], dtypes.int64)

rt = RaggedTensor.from_row_limits(values, row_limits, validate=False)
self.assertEqual(rt.dtype, dtypes.string)
self.assertEqual(rt.shape.as_list(), [5, None])
self.assertEqual(rt.ragged_rank, 1)

rt_values = rt.values
rt_row_limits = rt.row_limits()
rt_nrows = rt.nrows()

self.assertIs(rt_values, values)
self.assertAllEqual(rt_nrows, 5)
self.assertAllEqual(rt_row_limits, row_limits)
self.assertAllEqual(rt,
                    [[b'a', b'b'], [], [b'c', b'd', b'e'], [b'f'], [b'g']])
