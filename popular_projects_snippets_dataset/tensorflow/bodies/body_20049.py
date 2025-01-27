# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding.py
"""Send gradient to TPU embedding.

    Args:
      feature_to_gradient_dict: dict mapping feature names to gradient wrt
        activations.
      step: the current global step, used for dynamic learning rate.

    Returns:
      SendTPUEmbeddingGradients Op.

    Raises:
      RuntimeError: If `mode` is not `TRAINING`.
    """
if self._mode != TRAINING:
    raise RuntimeError('Only in training mode gradients need to '
                       'be sent to TPU embedding; got mode {}.'.format(
                           self._mode))
if step is None and self._learning_rate_fn:
    raise ValueError('There are dynamic learning rates but step is None.')

gradients = []
for table in self._table_to_features_dict:
    for feature in self._table_to_features_dict[table]:
        gradients.append(feature_to_gradient_dict[feature])

exit(tpu_ops.send_tpu_embedding_gradients(
    inputs=gradients,
    learning_rates=[
        math_ops.cast(fn(step), dtype=dtypes.float32)
        for fn in self._learning_rate_fn
    ],
    config=self.config_proto.SerializeToString()))
