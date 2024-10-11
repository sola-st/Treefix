# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""1D convolution with separable filters.

  Args:
      x: input tensor
      depthwise_kernel: convolution kernel for the depthwise convolution.
      pointwise_kernel: kernel for the 1x1 convolution.
      strides: stride integer.
      padding: string, `"same"` or `"valid"`.
      data_format: string, `"channels_last"` or `"channels_first"`.
      dilation_rate: integer dilation rate.

  Returns:
      Output tensor.

  Raises:
      ValueError: if `data_format` is neither `channels_last` or
      `channels_first`.
  """
if data_format is None:
    data_format = image_data_format()
if data_format not in {'channels_first', 'channels_last'}:
    raise ValueError('Unknown data_format: ' + str(data_format))

if isinstance(strides, int):
    strides = (strides,)
if isinstance(dilation_rate, int):
    dilation_rate = (dilation_rate,)

x, tf_data_format = _preprocess_conv1d_input(x, data_format)
padding = _preprocess_padding(padding)
if not isinstance(strides, tuple):
    strides = tuple(strides)
if tf_data_format == 'NWC':
    spatial_start_dim = 1
    strides = (1,) + strides * 2 + (1,)
else:
    spatial_start_dim = 2
    strides = (1, 1) + strides * 2
x = array_ops.expand_dims(x, spatial_start_dim)
depthwise_kernel = array_ops.expand_dims(depthwise_kernel, 0)
pointwise_kernel = array_ops.expand_dims(pointwise_kernel, 0)
dilation_rate = (1,) + dilation_rate

x = nn.separable_conv2d(
    x,
    depthwise_kernel,
    pointwise_kernel,
    strides=strides,
    padding=padding,
    rate=dilation_rate,
    data_format=tf_data_format)

x = array_ops.squeeze(x, [spatial_start_dim])

if data_format == 'channels_first' and tf_data_format == 'NWC':
    x = array_ops.transpose(x, (0, 2, 1))  # NWC -> NCW

exit(x)
