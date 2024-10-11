# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v1.py
super(TPUEmbeddingV0, self).__init__(feature_config, optimizer)
self._strategy = distribution_strategy_context.get_strategy()
if not isinstance(self._strategy,
                  (tpu_strategy.TPUStrategy, tpu_strategy.TPUStrategyV2)):
    raise RuntimeError(
        "TPUEmbeddingV0 should be created under TPUStrategy but found {}."
        .format(self._strategy))
self._built = False
