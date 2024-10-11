# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipForDeviceType(['TPU', 'GPU'],
                       'Strings only for CPUs, this is a host-only op.')

basename = constant_op.constant('dtensor-file')
shard = constant_op.constant(1, dtype=dtypes.int32)
num_shards = constant_op.constant(16, dtype=dtypes.int32)

layout = Layout.replicated(self.mesh, rank=0)

expected = gen_io_ops.sharded_filename(
    basename=basename, shard=shard, num_shards=num_shards, name=None)

result = gen_io_ops.sharded_filename(
    basename=numpy_util.pack_numpy(basename, layout),
    shard=numpy_util.pack_numpy(shard, layout),
    num_shards=numpy_util.pack_numpy(num_shards, layout))

self.assertEqual(api.fetch_layout(result), layout)
for result_tensor in api.unpack(result):
    self.assertEqual(expected, result_tensor)
