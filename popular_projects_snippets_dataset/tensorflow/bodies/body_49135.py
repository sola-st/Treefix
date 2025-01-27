# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Resizes the images contained in a 4D tensor.

  Args:
      x: Tensor or variable to resize.
      height_factor: Positive integer.
      width_factor: Positive integer.
      data_format: One of `"channels_first"`, `"channels_last"`.
      interpolation: A string, one of `nearest` or `bilinear`.

  Returns:
      A tensor.

  Raises:
      ValueError: in case of incorrect value for
        `data_format` or `interpolation`.
  """
if data_format == 'channels_first':
    rows, cols = 2, 3
elif data_format == 'channels_last':
    rows, cols = 1, 2
else:
    raise ValueError('Invalid `data_format` argument: %s' % (data_format,))

new_shape = x.shape[rows:cols + 1]
if new_shape.is_fully_defined():
    new_shape = constant_op.constant(new_shape.as_list(), dtype='int32')
else:
    new_shape = array_ops.shape_v2(x)[rows:cols + 1]
new_shape *= constant_op.constant(
    np.array([height_factor, width_factor], dtype='int32'))

if data_format == 'channels_first':
    x = permute_dimensions(x, [0, 2, 3, 1])
if interpolation == 'nearest':
    x = image_ops.resize_images_v2(
        x, new_shape, method=image_ops.ResizeMethod.NEAREST_NEIGHBOR)
elif interpolation == 'bilinear':
    x = image_ops.resize_images_v2(x, new_shape,
                                   method=image_ops.ResizeMethod.BILINEAR)
else:
    raise ValueError('interpolation should be one '
                     'of "nearest" or "bilinear".')
if data_format == 'channels_first':
    x = permute_dimensions(x, [0, 3, 1, 2])

exit(x)
