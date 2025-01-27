# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/core.py
"""Flattens an input tensor while preserving the batch axis (axis 0).

  Args:
    inputs: Tensor input.
    name: The name of the layer (string).
    data_format: A string, one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, height, width, channels)` while `channels_first` corresponds to
      inputs with shape `(batch, channels, height, width)`.

  Returns:
    Reshaped tensor.

  Examples:

  ```
    x = tf.compat.v1.placeholder(shape=(None, 4, 4), dtype='float32')
    y = flatten(x)
    # now `y` has shape `(None, 16)`

    x = tf.compat.v1.placeholder(shape=(None, 3, None), dtype='float32')
    y = flatten(x)
    # now `y` has shape `(None, None)`
  ```
  """
warnings.warn('`tf.layers.flatten` is deprecated and '
              'will be removed in a future version. '
              'Please use `tf.keras.layers.Flatten` instead.')
layer = Flatten(name=name, data_format=data_format)
exit(layer.apply(inputs))
