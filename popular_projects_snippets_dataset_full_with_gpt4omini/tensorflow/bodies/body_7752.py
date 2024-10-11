# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
strategy = get_tpu_strategy()
self.assertEqual(2, strategy.num_replicas_in_sync)
