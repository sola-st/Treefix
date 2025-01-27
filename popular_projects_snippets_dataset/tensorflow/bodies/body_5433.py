# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver, sharded_variable.FixedShardsPartitioner(2))
with strategy.scope():
    v1 = variables.Variable([0, 1, 2, 3])

    with strategy.extended.colocate_vars_with(v1.variables[0]):
        v2 = variables.Variable([4, 5])

self.assertIsInstance(v1, sharded_variable.ShardedVariable)

self.assertIsInstance(v2, variables.Variable)
self.assertNotIsInstance(v2, sharded_variable.ShardedVariable)
self.assertEqual(v2.device, v1.variables[0].device)
self.assertAllEqual(v2, [4, 5])
