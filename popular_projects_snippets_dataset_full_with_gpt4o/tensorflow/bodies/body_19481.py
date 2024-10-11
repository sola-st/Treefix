# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_initialization_test.py
resolver = tpu_cluster_resolver.TPUClusterResolver('')
tpu_strategy_util.initialize_tpu_system(resolver)
