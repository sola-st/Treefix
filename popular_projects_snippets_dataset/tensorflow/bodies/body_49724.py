# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/pooling.py
"""Average pooling layer for 2D inputs (e.g. images).

  Args:
    inputs: The tensor over which to pool. Must have rank 4.
    pool_size: An integer or tuple/list of 2 integers: (pool_height, pool_width)
      specifying the size of the pooling window.
      Can be a single integer to specify the same value for
      all spatial dimensions.
    strides: An integer or tuple/list of 2 integers,
      specifying the strides of the pooling operation.
      Can be a single integer to specify the same value for
      all spatial dimensions.
    padding: A string. The padding method, either 'valid' or 'same'.
      Case-insensitive.
    data_format: A string. The ordering of the dimensions in the inputs.
      `channels_last` (default) and `channels_first` are supported.
      `channels_last` corresponds to inputs with shape
      `(batch, height, width, channels)` while `channels_first` corresponds to
      inputs with shape `(batch, channels, height, width)`.
    name: A string, the name of the layer.

  Returns:
    Output tensor.

  Raises:
    ValueError: if eager execution is enabled.
  """
warnings.warn('`tf.layers.average_pooling2d` is deprecated and '
              'will be removed in a future version. '
              'Please use `tf.keras.layers.AveragePooling2D` instead.')
layer = AveragePooling2D(pool_size=pool_size, strides=strides,
                         padding=padding, data_format=data_format,
                         name=name)
exit(layer.apply(inputs))
