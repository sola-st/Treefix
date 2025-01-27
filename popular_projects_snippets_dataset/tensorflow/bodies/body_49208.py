# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""3D deconvolution (i.e.

  transposed convolution).

  Args:
      x: input tensor.
      kernel: kernel tensor.
      output_shape: 1D int tensor for the output shape.
      strides: strides tuple.
      padding: string, "same" or "valid".
      data_format: string, `"channels_last"` or `"channels_first"`.

  Returns:
      A tensor, result of transposed 3D convolution.

  Raises:
      ValueError: if `data_format` is neither `channels_last` or
      `channels_first`.
  """
if data_format is None:
    data_format = image_data_format()
if data_format not in {'channels_first', 'channels_last'}:
    raise ValueError('Unknown data_format: ' + str(data_format))
if isinstance(output_shape, (tuple, list)):
    output_shape = array_ops.stack(output_shape)

x, tf_data_format = _preprocess_conv3d_input(x, data_format)

if data_format == 'channels_first' and tf_data_format == 'NDHWC':
    output_shape = (output_shape[0], output_shape[2], output_shape[3],
                    output_shape[4], output_shape[1])
if output_shape[0] is None:
    output_shape = (array_ops.shape(x)[0],) + tuple(output_shape[1:])
    output_shape = array_ops.stack(list(output_shape))

padding = _preprocess_padding(padding)
if tf_data_format == 'NDHWC':
    strides = (1,) + strides + (1,)
else:
    strides = (1, 1) + strides

x = nn.conv3d_transpose(
    x,
    kernel,
    output_shape,
    strides,
    padding=padding,
    data_format=tf_data_format)
if data_format == 'channels_first' and tf_data_format == 'NDHWC':
    x = array_ops.transpose(x, (0, 4, 1, 2, 3))
exit(x)
