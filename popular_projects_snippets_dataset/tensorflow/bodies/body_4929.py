# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
partitioner = sharded_variable.MaxSizePartitioner(max_shard_bytes=4)
got = partitioner(tensor_shape.TensorShape([6, 1]), dtypes.float32)
self.assertAllEqual(got, [6, 1])

partitioner = sharded_variable.MaxSizePartitioner(
    max_shard_bytes=4, max_shards=2)
got = partitioner(tensor_shape.TensorShape([6, 1]), dtypes.float32)
self.assertAllEqual(got, [2, 1])

partitioner = sharded_variable.MaxSizePartitioner(max_shard_bytes=1024)
got = partitioner(tensor_shape.TensorShape([6, 1]), dtypes.float32)
self.assertAllEqual(got, [1, 1])
