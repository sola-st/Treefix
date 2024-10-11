# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)

coordinator_lib.ClusterCoordinator(strategy=strategy)

with strategy.scope():
    lookuptable = self.createStaticHashTable(
        init_source=source, vals=[0, 1, 2], default_value=-2)

self.assertIsInstance(lookuptable, ps_values.DistributedTable)
self.assertEqual(self.evaluate(lookuptable.size()), 3)

# Lookup on the coordinator.
output = lookuptable.lookup(
    constant_op.constant([0, 1, -1], dtype=dtypes.int64))
self.assertAllEqual([0, 1, -2], output)
self.assertEqual(lookuptable.size(), 3)
