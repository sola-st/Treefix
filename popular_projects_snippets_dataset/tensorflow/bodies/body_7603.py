# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
resolver = get_tpu_cluster_resolver()
remote.connect_to_cluster(resolver)
tpu_strategy_util.initialize_tpu_system(resolver)
strategy = tpu_lib.TPUStrategyV2(resolver)
strategy._enable_packed_variable_in_eager_mode = enable_packed_var
exit(strategy)
