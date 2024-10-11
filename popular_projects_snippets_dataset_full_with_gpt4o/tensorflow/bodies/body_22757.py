# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/experimental/xla_sharding_test.py
"""Tests the various recommended ways to construct a Sharding object.

    This is the most minimal of tests, doesn't assert anything about the
    Sharding object produced by a given factory methods other than that it
    has the correct type.
    """
self.assertIsInstance(xla_sharding.Sharding.replicate(),
                      xla_sharding.Sharding)
self.assertIsInstance(xla_sharding.Sharding.manual(), xla_sharding.Sharding)
self.assertIsInstance(
    xla_sharding.Sharding.assign_device(0), xla_sharding.Sharding)
self.assertIsInstance(
    xla_sharding.Sharding.tile(np.ones([3], dtype=int)),
    xla_sharding.Sharding)
self.assertIsInstance(
    xla_sharding.Sharding.partial_tile(np.ones([3], dtype=int)),
    xla_sharding.Sharding)
self.assertIsInstance(
    xla_sharding.Sharding.split(
        array_ops.ones([3, 8, 7], dtype=dtypes.int32), 1, 2),
    xla_sharding.Sharding)
self.assertIsInstance(
    xla_sharding.Sharding.subgroup_tile(
        np.ones([2, 3, 3], dtype=int), [
            xla_data_pb2.OpSharding.REPLICATED,
            xla_data_pb2.OpSharding.MANUAL
        ]), xla_sharding.Sharding)
