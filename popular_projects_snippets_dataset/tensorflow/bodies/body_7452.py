# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
strategy = mirrored_strategy.MirroredStrategy(self.mesh)
self.assertFalse(strategy.extended._in_multi_worker_mode())
