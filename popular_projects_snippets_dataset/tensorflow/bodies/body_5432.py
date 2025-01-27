# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
# For small variables there is only one partition.
variable_partitioner = sharded_variable.MinSizePartitioner(
    min_shard_bytes=64 << 20, max_shards=2)
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, variable_partitioner)
with strategy.scope():
    initializer = init_ops_v2.Constant([0] * 10)
    v1 = variables.Variable(
        initial_value=lambda: initializer(shape=(10,), dtype=dtypes.int64),
        shape=(10,),
        dtype=dtypes.int64)

    v2 = variables.Variable([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

self.assertIsInstance(v1, variables.Variable)
self.assertNotIsInstance(v1, sharded_variable.ShardedVariable)
self.assertRegex(v1.device, "/job:ps/replica:0/task:0")
self.assertAllEqual(v1, [0] * 10)

self.assertIsInstance(v2, variables.Variable)
self.assertNotIsInstance(v2, sharded_variable.ShardedVariable)
self.assertRegex(v2.device, "/job:ps/replica:0/task:1")
self.assertAllEqual(v2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
