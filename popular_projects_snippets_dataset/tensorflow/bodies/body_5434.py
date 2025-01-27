# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, sharded_variable.FixedShardsPartitioner(2))
with strategy.scope():
    initializer = PartitionAwareIdentity()
    initial_value = functools.partial(
        initializer, shape=(4, 4), dtype=dtypes.int64)
    v = variables.Variable(
        initial_value=initial_value, shape=(4, 4), dtype=dtypes.int64)

self.assertIsInstance(v, sharded_variable.ShardedVariable)
self.assertLen(v.variables, 2)
self.assertRegex(v.variables[0].device, "/job:ps/replica:0/task:0")
self.assertRegex(v.variables[1].device, "/job:ps/replica:0/task:1")
self.assertAllEqual(v.variables[0], [[1, 0, 0, 0], [0, 1, 0, 0]])
self.assertAllEqual(v.variables[1], [[0, 0, 1, 0], [0, 0, 0, 1]])
