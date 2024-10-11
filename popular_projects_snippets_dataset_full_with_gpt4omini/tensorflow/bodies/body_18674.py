# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2_test.py
full_shape = (4, 2)
partition_shape = (2, 2)
partition_offset = (0, 0)
full_value = self.evaluate(init(full_shape, dtype=dtypes.float32))
got = self.evaluate(
    init(
        full_shape,
        dtype=dtypes.float32,
        partition_shape=partition_shape,
        partition_offset=partition_offset))
self.assertEqual(got.shape, partition_shape)
self.assertAllClose(
    got, array_ops.slice(full_value, partition_offset, partition_shape))
