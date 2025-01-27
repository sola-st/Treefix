# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/pooling.py
"""Max Pooling layer for 1D inputs.

  Args:
    inputs: The tensor over which to pool. Must have rank 3.
    pool_size: An integer or tuple/list of a single integer,
      representing the size of the pooling window.
    strides: An integer or tuple/list of a single integer, specifying the
      strides of the pooling operation.
    padding: A string. The padding method, either 'valid' or 'same'.
      Case-insensitive.
    data_format: A string, one of `channels_last` (default) or `channels_first`.
      The ordering of the dimensions in the inputs.
      `channels_last` corresponds to inputs with shape
      `(batch, length, channels)` while `channels_first` corresponds to
      inputs with shape `(batch, channels, length)`.
    name: A string, the name of the layer.

  Returns:
    The output tensor, of rank 3.

  Raises:
    ValueError: if eager execution is enabled.
  """
warnings.warn('`tf.layers.max_pooling1d` is deprecated and '
              'will be removed in a future version. '
              'Please use `tf.keras.layers.MaxPooling1D` instead.')
layer = MaxPooling1D(pool_size=pool_size,
                     strides=strides,
                     padding=padding,
                     data_format=data_format,
                     name=name)
exit(layer.apply(inputs))
