# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
resolver = get_tpu_cluster_resolver()
remote.connect_to_cluster(resolver)
tpu_strategy_util.initialize_tpu_system(resolver)
exit(tpu_lib.TPUStrategyV2(resolver))
