# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_getitem_test.py
# rt: [[[['a', 'b'], ['c', 'd']], [], [['e', 'f']]], []]
splits1 = [0, 3, 3]
splits2 = [0, 2, 2, 3]
values = constant_op.constant([['a', 'b'], ['c', 'd'], ['e', 'f']])
rt = RaggedTensor.from_nested_row_splits(values, [splits1, splits2])
rt_newaxis0 = rt[array_ops.newaxis]
rt_newaxis1 = rt[:, array_ops.newaxis]
rt_newaxis2 = rt[:, :, array_ops.newaxis]
rt_newaxis3 = rt[:, :, :, array_ops.newaxis]
rt_newaxis4 = rt[:, :, :, :, array_ops.newaxis]

self.assertAllEqual(
    rt, [[[[b'a', b'b'], [b'c', b'd']], [], [[b'e', b'f']]], []])
self.assertAllEqual(
    rt_newaxis0, [[[[[b'a', b'b'], [b'c', b'd']], [], [[b'e', b'f']]], []]])
self.assertAllEqual(
    rt_newaxis1,
    [[[[[b'a', b'b'], [b'c', b'd']], [], [[b'e', b'f']]]], [[]]])
self.assertAllEqual(
    rt_newaxis2,
    [[[[[b'a', b'b'], [b'c', b'd']]], [[]], [[[b'e', b'f']]]], []])
self.assertAllEqual(
    rt_newaxis3,
    [[[[[b'a', b'b']], [[b'c', b'd']]], [], [[[b'e', b'f']]]], []])
self.assertAllEqual(
    rt_newaxis4,
    [[[[[b'a'], [b'b']], [[b'c'], [b'd']]], [], [[[b'e'], [b'f']]]], []])

self.assertEqual(rt.ragged_rank, 2)
self.assertEqual(rt_newaxis0.ragged_rank, 3)
self.assertEqual(rt_newaxis1.ragged_rank, 3)
self.assertEqual(rt_newaxis2.ragged_rank, 3)
self.assertEqual(rt_newaxis3.ragged_rank, 2)
self.assertEqual(rt_newaxis4.ragged_rank, 2)

self.assertEqual(rt_newaxis0.shape.as_list(), [1, 2, None, None, 2])
self.assertEqual(rt_newaxis1.shape.as_list(), [2, 1, None, None, 2])
self.assertEqual(rt_newaxis2.shape.as_list(), [2, None, 1, None, 2])
self.assertEqual(rt_newaxis3.shape.as_list(), [2, None, None, 1, 2])
self.assertEqual(rt_newaxis4.shape.as_list(), [2, None, None, 2, 1])
