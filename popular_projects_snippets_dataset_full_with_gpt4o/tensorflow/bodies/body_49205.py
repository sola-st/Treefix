# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""2D convolution with separable filters.

  Args:
      x: input tensor
      depthwise_kernel: convolution kernel for the depthwise convolution.
      pointwise_kernel: kernel for the 1x1 convolution.
      strides: strides tuple (length 2).
      padding: string, `"same"` or `"valid"`.
      data_format: string, `"channels_last"` or `"channels_first"`.
      dilation_rate: tuple of integers,
          dilation rates for the separable convolution.

  Returns:
      Output tensor.

  Raises:
      ValueError: if `data_format` is neither `channels_last` or
      `channels_first`.
      ValueError: if `strides` is not a tuple of 2 integers.
  """
if data_format is None:
    data_format = image_data_format()
if data_format not in {'channels_first', 'channels_last'}:
    raise ValueError('Unknown data_format: ' + str(data_format))
if len(strides) != 2:
    raise ValueError('`strides` must be a tuple of 2 integers.')

x, tf_data_format = _preprocess_conv2d_input(x, data_format)
padding = _preprocess_padding(padding)
if not isinstance(strides, tuple):
    strides = tuple(strides)
if tf_data_format == 'NHWC':
    strides = (1,) + strides + (1,)
else:
    strides = (1, 1) + strides

x = nn.separable_conv2d(
    x,
    depthwise_kernel,
    pointwise_kernel,
    strides=strides,
    padding=padding,
    rate=dilation_rate,
    data_format=tf_data_format)
if data_format == 'channels_first' and tf_data_format == 'NHWC':
    x = array_ops.transpose(x, (0, 3, 1, 2))  # NHWC -> NCHW
exit(x)
