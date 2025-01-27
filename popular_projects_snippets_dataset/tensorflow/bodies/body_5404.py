# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils_test.py
def create_placeholder(shape, dtype):
    with ops.Graph().as_default():
        exit(array_ops.placeholder(dtype=dtype, shape=shape))

values = [
    array_ops.ones([10, 10], dtype=dtypes.float32),
    create_placeholder([None, 10], dtype=dtypes.float32),
]
packs = cross_device_utils.group_by_size(values, bytes_per_pack=1)
self.assertLen(packs, 1)
self.assertEqual(packs[0], values)
