# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, sharded_variable.FixedShardsPartitioner(4))
with strategy.scope():
    v = variables.Variable([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

self.assertIsInstance(v, sharded_variable.ShardedVariable)
self.assertLen(v.variables, 4)
self.assertRegex(v.variables[0].device, "/job:ps/replica:0/task:0")
self.assertRegex(v.variables[1].device, "/job:ps/replica:0/task:1")
self.assertRegex(v.variables[2].device, "/job:ps/replica:0/task:0")
self.assertRegex(v.variables[3].device, "/job:ps/replica:0/task:1")
self.assertAllEqual(v.variables[0], [0, 1, 2])
self.assertAllEqual(v.variables[1], [3, 4, 5])
self.assertAllEqual(v.variables[2], [6, 7])
self.assertAllEqual(v.variables[3], [8, 9])
