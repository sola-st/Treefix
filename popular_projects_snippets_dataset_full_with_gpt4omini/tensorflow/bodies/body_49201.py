# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""1D convolution.

  Args:
      x: Tensor or variable.
      kernel: kernel tensor.
      strides: stride integer.
      padding: string, `"same"`, `"causal"` or `"valid"`.
      data_format: string, one of "channels_last", "channels_first".
      dilation_rate: integer dilate rate.

  Returns:
      A tensor, result of 1D convolution.

  Raises:
      ValueError: if `data_format` is neither `channels_last` or
      `channels_first`.
  """
if data_format is None:
    data_format = image_data_format()
if data_format not in {'channels_first', 'channels_last'}:
    raise ValueError('Unknown data_format: ' + str(data_format))

kernel_shape = kernel.shape.as_list()
if padding == 'causal':
    # causal (dilated) convolution:
    left_pad = dilation_rate * (kernel_shape[0] - 1)
    x = temporal_padding(x, (left_pad, 0))
    padding = 'valid'
padding = _preprocess_padding(padding)

x, tf_data_format = _preprocess_conv1d_input(x, data_format)
x = nn.convolution(
    input=x,
    filter=kernel,
    dilation_rate=dilation_rate,
    strides=strides,
    padding=padding,
    data_format=tf_data_format)
if data_format == 'channels_first' and tf_data_format == 'NWC':
    x = array_ops.transpose(x, (0, 2, 1))  # NWC -> NCW
exit(x)
