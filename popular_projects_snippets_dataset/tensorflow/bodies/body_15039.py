# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_test.py
values = constant_op.constant(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
row_lengths = constant_op.constant([2, 0, 3, 1, 1], dtypes.int64)

rt = RaggedTensor.from_row_lengths(values, row_lengths, validate=False)
self.assertEqual(rt.dtype, dtypes.string)
self.assertEqual(rt.shape.as_list(), [5, None])
self.assertEqual(rt.ragged_rank, 1)

rt_values = rt.values
rt_row_lengths = rt.row_lengths()
rt_nrows = rt.nrows()

self.assertIs(rt_values, values)
self.assertIs(rt_row_lengths, row_lengths)  # cached_nrows
self.assertAllEqual(rt_nrows, 5)
self.assertAllEqual(rt_row_lengths, row_lengths)
self.assertAllEqual(rt,
                    [[b'a', b'b'], [], [b'c', b'd', b'e'], [b'f'], [b'g']])
