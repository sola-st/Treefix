# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
partitioner = sharded_variable.FixedShardsPartitioner(num_shards=2)
got = partitioner(tensor_shape.TensorShape([10, 3]), dtypes.float32)
self.assertAllEqual(got, [2, 1])
