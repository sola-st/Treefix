# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""2D Pooling.

  Args:
      x: Tensor or variable.
      pool_size: tuple of 2 integers.
      strides: tuple of 2 integers.
      padding: string, `"same"` or `"valid"`.
      data_format: string, `"channels_last"` or `"channels_first"`.
      pool_mode: string, `"max"` or `"avg"`.

  Returns:
      A tensor, result of 2D pooling.

  Raises:
      ValueError: if `data_format` is neither `"channels_last"` or
      `"channels_first"`.
      ValueError: if `pool_size` is not a tuple of 2 integers.
      ValueError: if `strides` is not a tuple of 2 integers.
      ValueError: if `pool_mode` is neither `"max"` or `"avg"`.
  """
if data_format is None:
    data_format = image_data_format()
if data_format not in {'channels_first', 'channels_last'}:
    raise ValueError('Unknown data_format: ' + str(data_format))
if len(pool_size) != 2:
    raise ValueError('`pool_size` must be a tuple of 2 integers.')
if len(strides) != 2:
    raise ValueError('`strides` must be a tuple of 2 integers.')

x, tf_data_format = _preprocess_conv2d_input(x, data_format)
padding = _preprocess_padding(padding)
if tf_data_format == 'NHWC':
    strides = (1,) + strides + (1,)
    pool_size = (1,) + pool_size + (1,)
else:
    strides = (1, 1) + strides
    pool_size = (1, 1) + pool_size

if pool_mode == 'max':
    x = nn.max_pool(
        x, pool_size, strides, padding=padding, data_format=tf_data_format)
elif pool_mode == 'avg':
    x = nn.avg_pool(
        x, pool_size, strides, padding=padding, data_format=tf_data_format)
else:
    raise ValueError('Invalid pooling mode: ' + str(pool_mode))

if data_format == 'channels_first' and tf_data_format == 'NHWC':
    x = array_ops.transpose(x, (0, 3, 1, 2))  # NHWC -> NCHW
exit(x)
