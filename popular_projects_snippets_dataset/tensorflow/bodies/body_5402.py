# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils_test.py
values = [
    array_ops.ones([1], dtype=dtypes.float32),
    array_ops.ones([2], dtype=dtypes.float32),
]
packs = cross_device_utils.group_by_size(values, bytes_per_pack=0)
self.assertLen(packs, 1)
self.assertLen(packs[0], 2)
self.assertEqual(packs[0][0].shape, [1])
self.assertEqual(packs[0][1].shape, [2])
