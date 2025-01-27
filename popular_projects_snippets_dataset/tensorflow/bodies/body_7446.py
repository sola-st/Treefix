# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
strategy = mirrored_strategy.MirroredStrategy(self.mesh)
self.assertIsInstance(strategy.extended, distribute_lib.StrategyExtendedV2)
