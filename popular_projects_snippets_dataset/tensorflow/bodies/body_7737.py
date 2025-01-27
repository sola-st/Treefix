# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy(enable_packed_var)
self.assertIsNotNone(strategy.cluster_resolver)
