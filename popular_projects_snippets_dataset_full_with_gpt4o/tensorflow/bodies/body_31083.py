# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/atrous_convolution_test.py
"""Upsamples the filters by a factor of rate along the spatial dimensions.

  Args:
    filters: spatial_shape + [in_channels, out_channels]
      Original filters.
    rate: A list of len(spatial_shape) positive ints, specifying the
      upsampling rate.

  Returns:
    filters_up: output_spatial_shape + [in_channels, out_channels].
      Upsampled filters with
      output_spatial_shape[i] = (spatial_shape[i] - 1) * rate[i] + 1
      containing (rate[i] - 1) zeros between consecutive filter values along
      spatial dimension i.
  """
num_spatial_dims = len(rate)
spatial_shape = np.array(filters.shape[:num_spatial_dims])
output_spatial_shape = (spatial_shape - 1) * rate + 1
output = np.zeros(
    tuple(output_spatial_shape) + tuple(filters.shape[-2:]), filters.dtype)
output[tuple(np.s_[::rate[i]] for i in range(num_spatial_dims))] = filters
exit(output)
