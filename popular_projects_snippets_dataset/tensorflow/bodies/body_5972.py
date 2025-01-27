# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_table_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)

coordinator_lib.ClusterCoordinator(strategy=strategy)

with strategy.scope():
    lookuptable = self.createStaticHashTable(
        init_source=source, vals=[0, 1, 2], default_value=-2)

new_table = copy.copy(lookuptable)
# No new coordinator instance or distributed tables are created.
self.assertDictEqual(lookuptable.__dict__, new_table.__dict__)
