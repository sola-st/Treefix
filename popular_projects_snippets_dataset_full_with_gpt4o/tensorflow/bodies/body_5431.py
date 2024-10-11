# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, sharded_variable.FixedShardsPartitioner(4))
with strategy.scope():
    v = variables.Variable([0, 1, 2])

self.assertIsInstance(v, sharded_variable.ShardedVariable)
self.assertLen(v.variables, 3)
self.assertRegex(v.variables[0].device, "/job:ps/replica:0/task:0")
self.assertRegex(v.variables[1].device, "/job:ps/replica:0/task:1")
self.assertRegex(v.variables[2].device, "/job:ps/replica:0/task:0")
self.assertAllEqual(v.variables[0], [0])
self.assertAllEqual(v.variables[1], [1])
self.assertAllEqual(v.variables[2], [2])
