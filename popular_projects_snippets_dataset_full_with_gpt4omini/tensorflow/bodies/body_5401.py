# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils_test.py
# Each packs except the last one should be equal or larger than
# bytes_per_pack.
values = [
    # size = 2 * 4 * 4 * 4 = 128
    array_ops.ones([2, 4, 4], dtype=dtypes.float32),
    # size = 8 * 4 = 32
    array_ops.ones([8], dtype=dtypes.int32),
    # size = 10 * 10 * 8 = 800
    array_ops.ones([10, 10], dtype=dtypes.int64),
    # size = 1 * 4 = 4
    array_ops.ones([1], dtype=dtypes.int32),
]
packs = cross_device_utils.group_by_size(values, bytes_per_pack=200)
self.assertLen(packs, 2)
self.assertLen(packs[0], 3)
self.assertEqual(packs[0][0].shape, [2, 4, 4])
self.assertEqual(packs[0][1].shape, [8])
self.assertEqual(packs[0][2].shape, [10, 10])
self.assertLen(packs[1], 1)
self.assertEqual(packs[1][0].shape, [1])
