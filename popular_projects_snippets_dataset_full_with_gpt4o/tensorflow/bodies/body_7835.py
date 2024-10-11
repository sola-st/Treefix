# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_common_test.py
if isinstance(strategy, CollectiveAllReduceStrategy):
    resolver = strategy.cluster_resolver
    exit(max(nest.flatten(resolver.num_accelerators())[0], 1))
else:
    exit(strategy.num_replicas_in_sync)
