# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipForDeviceType(
    ['GPU', 'TPU'],
    'StringToHashBucket functions not supported on TPU or GPU.')

inputs = constant_op.constant(['a', 'b', 'c', 'd'], dtype=dtypes.string)
expected_result = to_hash_bucket_fn(inputs, num_buckets=32)

if shard_spec == 'sharded':
    layout = Layout.batch_sharded(self.mesh, _MESH_DIM_X, rank=1)
else:
    layout = Layout.replicated(self.mesh, rank=1)
inputs = numpy_util.pack_numpy(inputs, layout)
got = to_hash_bucket_fn(inputs, num_buckets=32)

self.assertDTensorEqual(expected_result, layout, got)
