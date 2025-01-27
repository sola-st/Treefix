# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""3D convolution.

  Args:
      x: Tensor or variable.
      kernel: kernel tensor.
      strides: strides tuple.
      padding: string, `"same"` or `"valid"`.
      data_format: string, `"channels_last"` or `"channels_first"`.
      dilation_rate: tuple of 3 integers.

  Returns:
      A tensor, result of 3D convolution.

  Raises:
      ValueError: if `data_format` is neither `channels_last` or
      `channels_first`.
  """
if data_format is None:
    data_format = image_data_format()
if data_format not in {'channels_first', 'channels_last'}:
    raise ValueError('Unknown data_format: ' + str(data_format))

x, tf_data_format = _preprocess_conv3d_input(x, data_format)
padding = _preprocess_padding(padding)
x = nn.convolution(
    input=x,
    filter=kernel,
    dilation_rate=dilation_rate,
    strides=strides,
    padding=padding,
    data_format=tf_data_format)
if data_format == 'channels_first' and tf_data_format == 'NDHWC':
    x = array_ops.transpose(x, (0, 4, 1, 2, 3))
exit(x)
