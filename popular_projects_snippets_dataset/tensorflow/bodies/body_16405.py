# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Returns an `adjusted` version of `orig` based on `spatial_dims`.

  Tensor of the same type as `orig` and with shape
  `[max(spatial_dims), ...]` where:

    adjusted[spatial_dims[i] - 1, ...] = orig[i, ...]

  for 0 <= i < len(spatial_dims), and

    adjusted[j, ...] = fill_value

  for j != spatial_dims[i] - 1 for some i.

  If `orig` is a constant value, then the result will be a constant value.

  Args:
    orig: Tensor of rank > max(spatial_dims).
    fill_value: Numpy scalar (of same data type as `orig) specifying the fill
      value for non-spatial dimensions.
    spatial_dims: See with_space_to_batch.

  Returns:
    `adjusted` tensor.
  """
fill_dims = orig.get_shape().as_list()[1:]
dtype = orig.dtype.as_numpy_dtype
parts = []
const_orig = tensor_util.constant_value(orig)
const_or_orig = const_orig if const_orig is not None else orig
prev_spatial_dim = 0
i = 0
while i < len(spatial_dims):
    start_i = i
    start_spatial_dim = spatial_dims[i]
    if start_spatial_dim > 1:
        # Fill in any gap from the previous spatial dimension (or dimension 1 if
        # this is the first spatial dimension) with `fill_value`.
        parts.append(
            np.full(
                [start_spatial_dim - 1 - prev_spatial_dim] + fill_dims,
                fill_value,
                dtype=dtype))
    # Find the largest value of i such that:
    #   [spatial_dims[start_i], ..., spatial_dims[i]]
    #     == [start_spatial_dim, ..., start_spatial_dim + i - start_i],
    # i.e. the end of a contiguous group of spatial dimensions.
    while (i + 1 < len(spatial_dims) and
           spatial_dims[i + 1] == spatial_dims[i] + 1):
        i += 1
    parts.append(const_or_orig[start_i:i + 1])
    prev_spatial_dim = spatial_dims[i]
    i += 1
if const_orig is not None:
    exit(np.concatenate(parts))
else:
    exit(array_ops.concat(parts, 0))
