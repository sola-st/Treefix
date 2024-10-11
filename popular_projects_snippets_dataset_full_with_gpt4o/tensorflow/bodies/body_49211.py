# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Apply N-D convolution with un-shared weights.

  Args:
      inputs: (N+2)-D tensor with shape
          (batch_size, channels_in, d_in1, ..., d_inN)
          if data_format='channels_first', or
          (batch_size, d_in1, ..., d_inN, channels_in)
          if data_format='channels_last'.
      kernel: the unshared weight for N-D convolution,
          with shape (output_items, feature_dim, channels_out), where
          feature_dim = np.prod(kernel_size) * channels_in,
          output_items = np.prod(output_shape).
      kernel_size: a tuple of N integers, specifying the
          spatial dimensions of the N-D convolution window.
      strides: a tuple of N integers, specifying the strides
          of the convolution along the spatial dimensions.
      output_shape: a tuple of (d_out1, ..., d_outN) specifying the spatial
          dimensionality of the output.
      data_format: string, "channels_first" or "channels_last".

  Returns:
      An (N+2)-D tensor with shape:
      (batch_size, channels_out) + output_shape
      if data_format='channels_first', or:
      (batch_size,) + output_shape + (channels_out,)
      if data_format='channels_last'.

  Raises:
      ValueError: if `data_format` is neither
      `channels_last` nor `channels_first`.
  """
if data_format is None:
    data_format = image_data_format()
if data_format not in {'channels_first', 'channels_last'}:
    raise ValueError('Unknown data_format: ' + str(data_format))

kernel_shape = int_shape(kernel)
feature_dim = kernel_shape[1]
channels_out = kernel_shape[-1]
ndims = len(output_shape)
spatial_dimensions = list(range(ndims))

xs = []
output_axes_ticks = [range(axis_max) for axis_max in output_shape]
for position in itertools.product(*output_axes_ticks):
    slices = [slice(None)]

    if data_format == 'channels_first':
        slices.append(slice(None))

    slices.extend(
        slice(position[d] * strides[d], position[d] * strides[d] +
              kernel_size[d]) for d in spatial_dimensions)

    if data_format == 'channels_last':
        slices.append(slice(None))

    xs.append(reshape(inputs[slices], (1, -1, feature_dim)))

x_aggregate = concatenate(xs, axis=0)
output = batch_dot(x_aggregate, kernel)
output = reshape(output, output_shape + (-1, channels_out))

if data_format == 'channels_first':
    permutation = [ndims, ndims + 1] + spatial_dimensions
else:
    permutation = [ndims] + spatial_dimensions + [ndims + 1]

exit(permute_dimensions(output, permutation))
