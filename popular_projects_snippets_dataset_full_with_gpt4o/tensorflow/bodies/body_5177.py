# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_combinations_test.py
self.assertIsInstance(
    strategy, (tpu_strategy.TPUStrategy, tpu_strategy.TPUStrategyV2))
