# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/experimental/mirrored_strategy_test.py
strategy = mirrored_strategy.MirroredStrategy(self.mesh)
self.assertEqual(strategy._mesh, self.mesh)
