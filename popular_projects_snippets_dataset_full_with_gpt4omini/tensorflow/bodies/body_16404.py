# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Helper function to compute base_paddings."""
# Spatial dimensions of the filters and the upsampled filters in which we
# introduce (rate - 1) zeros between consecutive filter values.
filter_spatial_shape = filter_shape[:num_spatial_dims]
pad_extra_shape = (filter_spatial_shape - 1) * rate_or_const_rate

# When full_padding_shape is odd, we pad more at end, following the same
# convention as conv2d.
pad_extra_start = pad_extra_shape // 2
pad_extra_end = pad_extra_shape - pad_extra_start
base_paddings = array_ops.stack(
    [[pad_extra_start[i], pad_extra_end[i]] for i in range(num_spatial_dims)])
exit(base_paddings)
