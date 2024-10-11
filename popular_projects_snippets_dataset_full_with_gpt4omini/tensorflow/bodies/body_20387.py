# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_for_serving.py
"""Creates the TPUEmbeddingForServing mid level API object.

    ```python
    embedding = tf.tpu.experimental.embedding.TPUEmbeddingForServing(
        feature_config=tf.tpu.experimental.embedding.FeatureConfig(
            table=tf.tpu.experimental.embedding.TableConfig(
                dim=...,
                vocabulary_size=...)))
    ```

    Args:
      feature_config: A nested structure of
        `tf.tpu.experimental.embedding.FeatureConfig` configs.
      optimizer: An instance of one of `tf.tpu.experimental.embedding.SGD`,
        `tf.tpu.experimental.embedding.Adagrad` or
        `tf.tpu.experimental.embedding.Adam`. When not created under TPUStrategy
        may be set to None to avoid the creation of the optimizer slot
        variables, useful for optimizing memory consumption when exporting the
        model for serving where slot variables aren't needed.

    Raises:
      RuntimeError: If created under TPUStrategy.
    """
super(TPUEmbeddingForServing, self).__init__(feature_config, optimizer)
self._strategy = distribution_strategy_context.get_strategy()
if isinstance(self._strategy,
              (tpu_strategy.TPUStrategy, tpu_strategy.TPUStrategyV2)):
    raise RuntimeError("Serving on TPU is not yet supported.")
