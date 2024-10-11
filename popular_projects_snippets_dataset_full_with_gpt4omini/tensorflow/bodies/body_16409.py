# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Internal function which performs rank agnostic convolution.

  Args:
    input: See `convolution`.
    filters: See `convolution`.
    strides: See `convolution`.
    padding: See `convolution`.
    data_format: See `convolution`.
    dilations: See `convolution`.
    name: See `convolution`.
    call_from_convolution: See `convolution`.
    num_spatial_dims: (Optional.).  It is a integer describing the
      rank of the spatial dimensions.  For `1-D`, `2-D` and `3-D` convolutions,
      the value of `num_spatial_dims` is `1`, `2`, and `3`, respectively.
      This argument is only required to disambiguate the rank of `batch_shape`
      when `filter_shape.ndims is None` and `len(batch_shape) > 1`.  For
      backwards compatibility, if `num_spatial_dims is None` and
     `filter_shape.ndims is None`, then `len(batch_shape)` is assumed to be
     `1` (i.e., the input is expected to be
     `[batch_size, num_channels] + input_spatial_shape`
     or `[batch_size] + input_spatial_shape + [num_channels]`.

  Returns:
    A tensor of shape and dtype matching that of `input`.

  Raises:
    ValueError: If input and filter both have unknown shapes, or if
      `num_spatial_dims` is provided and incompatible with the value
      estimated from `filters.shape`.
  """
if (not isinstance(filters, variables_lib.Variable) and
    not tensor_util.is_tf_type(filters)):
    with ops.name_scope("convolution_internal", None, [filters, input]):
        filters = ops.convert_to_tensor(filters, name='filters')
if (not isinstance(input, ops.Tensor) and not tensor_util.is_tf_type(input)):
    with ops.name_scope("convolution_internal", None, [filters, input]):
        input = ops.convert_to_tensor(input, name="input")

filters_rank = filters.shape.rank
inputs_rank = input.shape.rank
if num_spatial_dims is None:
    if filters_rank:
        num_spatial_dims = filters_rank - 2
    elif inputs_rank:
        num_spatial_dims = inputs_rank - 2
    else:
        raise ValueError(
            "When `num_spatial_dims` is not set, one of `input.shape.rank` or "
            "`filters.shape.rank` must be known. "
            f"Received: input.shape={input.shape} of rank {inputs_rank} and "
            f"filters.shape={filters.shape} of rank {filters_rank}")
elif filters_rank and filters_rank - 2 != num_spatial_dims:
    raise ValueError(
        "`filters.shape.rank - 2` should equal `num_spatial_dims`. Received: "
        f"filters.shape={filters.shape} of rank {filters_rank} and "
        f"num_spatial_dims={num_spatial_dims}")

if inputs_rank:
    num_batch_dims = inputs_rank - num_spatial_dims - 1  # Channel dimension.
else:
    num_batch_dims = 1  # By default, assume single batch dimension.

if num_spatial_dims not in {1, 2, 3}:
    raise ValueError(
        "`num_spatial_dims` must be 1, 2, or 3. "
        f"Received: num_spatial_dims={num_spatial_dims}.")

if data_format is None or data_format in _CHANNELS_LAST_FORMATS:
    channel_index = num_batch_dims + num_spatial_dims
else:
    channel_index = num_batch_dims

if dilations is None:
    dilations = _get_sequence(dilations, num_spatial_dims, channel_index,
                              "dilations")
    is_dilated_conv = False
else:
    dilations = _get_sequence(dilations, num_spatial_dims, channel_index,
                              "dilations")
    is_dilated_conv = any(i != 1 for i in dilations)

strides = _get_sequence(strides, num_spatial_dims, channel_index, "strides")
has_tpu_context = device_context.enclosing_tpu_context() is not None

if name:
    default_name = None
elif not has_tpu_context or call_from_convolution:
    default_name = "convolution"
elif num_spatial_dims == 2:  # Most common case.
    default_name = "Conv2D"
elif num_spatial_dims == 3:
    default_name = "Conv3D"
else:
    default_name = "conv1d"

with ops.name_scope(name, default_name, [input, filters]) as name:
    # Fast path for TPU or if no dilation, as gradient only supported on TPU
    # for dilations.
    if not is_dilated_conv or has_tpu_context:
        if num_spatial_dims == 2:  # Most common case.
            op = _conv2d_expanded_batch
        elif num_spatial_dims == 3:
            op = _conv3d_expanded_batch
        else:
            op = conv1d

        exit(op(
            input,
            filters,
            strides,
            padding=padding,
            data_format=data_format,
            dilations=dilations,
            name=name))
    else:
        if channel_index == 1:
            strides = strides[2:]
            dilations = dilations[2:]
        else:
            strides = strides[1:-1]
            dilations = dilations[1:-1]

        op = Convolution(
            tensor_shape.as_shape(input.shape),
            tensor_shape.as_shape(filters.shape),
            padding,
            strides=strides,
            dilation_rate=dilations,
            name=name,
            data_format=data_format,
            num_spatial_dims=num_spatial_dims)
        exit(op(input, filters))
