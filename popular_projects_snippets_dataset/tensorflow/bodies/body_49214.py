# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Adds a bias vector to a tensor.

  Args:
      x: Tensor or variable.
      bias: Bias tensor to add.
      data_format: string, `"channels_last"` or `"channels_first"`.

  Returns:
      Output tensor.

  Raises:
      ValueError: In one of the two cases below:
                  1. invalid `data_format` argument.
                  2. invalid bias shape.
                     the bias should be either a vector or
                     a tensor with ndim(x) - 1 dimension
  """
if data_format is None:
    data_format = image_data_format()
if data_format not in {'channels_first', 'channels_last'}:
    raise ValueError('Unknown data_format: ' + str(data_format))
bias_shape = int_shape(bias)
if len(bias_shape) != 1 and len(bias_shape) != ndim(x) - 1:
    raise ValueError(
        'Unexpected bias dimensions %d, expect to be 1 or %d dimensions' %
        (len(bias_shape), ndim(x) - 1))

if len(bias_shape) == 1:
    if data_format == 'channels_first':
        exit(nn.bias_add(x, bias, data_format='NCHW'))
    exit(nn.bias_add(x, bias, data_format='NHWC'))
if ndim(x) in (3, 4, 5):
    if data_format == 'channels_first':
        bias_reshape_axis = (1, bias_shape[-1]) + bias_shape[:-1]
        exit(x + reshape(bias, bias_reshape_axis))
    exit(x + reshape(bias, (1,) + bias_shape))
exit(nn.bias_add(x, bias))
