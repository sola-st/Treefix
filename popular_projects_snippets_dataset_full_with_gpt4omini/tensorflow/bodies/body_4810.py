# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""Returns whether the strategy is a TPU strategy."""
exit(isinstance(strategy,
                  (tpu_strategy.TPUStrategy, tpu_strategy.TPUStrategyV1,
                   tpu_strategy.TPUStrategyV2)))
