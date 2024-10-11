# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_compilation_test.py
resolver = get_tpu_cluster_resolver()
remote.connect_to_cluster(resolver)
tpu_strategy_util.initialize_tpu_system(resolver)
strategy = tpu_lib.TPUStrategyV2(resolver)
exit(strategy)
