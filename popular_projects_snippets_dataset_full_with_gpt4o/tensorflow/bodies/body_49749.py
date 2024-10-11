# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/core.py
"""Applies Dropout to the input.

  Dropout consists in randomly setting a fraction `rate` of input units to 0
  at each update during training time, which helps prevent overfitting.
  The units that are kept are scaled by `1 / (1 - rate)`, so that their
  sum is unchanged at training time and inference time.

  Args:
    inputs: Tensor input.
    rate: The dropout rate, between 0 and 1. E.g. "rate=0.1" would drop out
      10% of input units.
    noise_shape: 1D tensor of type `int32` representing the shape of the
      binary dropout mask that will be multiplied with the input.
      For instance, if your inputs have shape
      `(batch_size, timesteps, features)`, and you want the dropout mask
      to be the same for all timesteps, you can use
      `noise_shape=[batch_size, 1, features]`.
    seed: A Python integer. Used to create random seeds. See
      `tf.compat.v1.set_random_seed`
      for behavior.
    training: Either a Python boolean, or a TensorFlow boolean scalar tensor
      (e.g. a placeholder). Whether to return the output in training mode
      (apply dropout) or in inference mode (return the input untouched).
    name: The name of the layer (string).

  Returns:
    Output tensor.

  Raises:
    ValueError: if eager execution is enabled.
  """
warnings.warn('`tf.layers.dropout` is deprecated and '
              'will be removed in a future version. '
              'Please use `tf.keras.layers.Dropout` instead.')
layer = Dropout(rate, noise_shape=noise_shape, seed=seed, name=name)
exit(layer.apply(inputs, training=training))
