# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable_test.py
if num_shards > 1:
    strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
        self.cluster_resolver,
        variable_partitioner=sharded_variable.FixedShardsPartitioner(
            num_shards))
else:
    strategy = ds_context._get_default_strategy()
exit(strategy)
