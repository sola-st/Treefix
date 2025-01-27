# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Helper function for convolution."""
num_batch_dims = None
filter_shape = tensor_shape.as_shape(filter_shape)
input_shape = tensor_shape.as_shape(input_shape)

if filter_shape.ndims is not None:
    if (num_spatial_dims is not None and
        filter_shape.ndims != num_spatial_dims + 2):
        raise ValueError(
            "`filters.shape.rank` must be `num_spatial_dims + 2`. Received: "
            f"filters.shape={filter_shape} of rank {filter_shape.rank} and "
            f"num_spatial_dims={num_spatial_dims}")
    else:
        num_spatial_dims = filter_shape.ndims - 2

if input_shape.ndims is not None and num_spatial_dims is not None:
    num_batch_dims = input_shape.ndims - num_spatial_dims - 1

if num_spatial_dims is None:
    num_spatial_dims = input_shape.ndims - 2
else:
    if input_shape.ndims is not None:
        if input_shape.ndims < num_spatial_dims + 2:
            raise ValueError(
                "`input.shape.rank` must be >= than `num_spatial_dims + 2`. "
                f"Received: input.shape={input_shape} of rank {input_shape.rank} "
                f"and num_spatial_dims={num_spatial_dims}")
        else:
            if num_batch_dims is None:
                num_batch_dims = input_shape.ndims - num_spatial_dims - 1

if num_spatial_dims is None:
    raise ValueError(
        "When `num_spatial_dims` is not set, one of `input.shape.rank` or "
        "`filters.shape.rank` must be known. "
        f"Received: input.shape={input_shape} of rank {input_shape.rank} and "
        f"`filters.shape={filter_shape}` of rank {filter_shape.rank}")

if num_batch_dims is None:
    num_batch_dims = 1

if num_batch_dims < 1:
    raise ValueError(
        f"Batch dims should be >= 1, but found {num_batch_dims}. "
        "Batch dims was estimated as "
        "`input.shape.rank - num_spatial_dims - 1` and `num_spatial_dims` "
        "was either provided or estimated as `filters.shape.rank - 2`. "
        f"Received: input.shape={input_shape} of rank {input_shape.rank}, "
        f"filters.shape={filter_shape} of rank {filter_shape.rank}, and "
        f"num_spatial_dims={num_spatial_dims}")

if data_format is None or not data_format.startswith("NC"):
    input_channels_dim = tensor_shape.dimension_at_index(
        input_shape, num_spatial_dims + num_batch_dims)
    spatial_dims = range(num_batch_dims, num_spatial_dims + num_batch_dims)
else:
    input_channels_dim = tensor_shape.dimension_at_index(
        input_shape, num_batch_dims)
    spatial_dims = range(
        num_batch_dims + 1, num_spatial_dims + num_batch_dims + 1)

filter_dim = tensor_shape.dimension_at_index(filter_shape, num_spatial_dims)
if not (input_channels_dim % filter_dim).is_compatible_with(0):
    raise ValueError(
        "The number of input channels is not divisible by the corresponding "
        f"number of output filters. Received: input.shape={input_shape} with "
        f"{input_channels_dim} channels and filters.shape={filter_shape} "
        f"with {filter_dim} output filters.")

strides, dilation_rate = _get_strides_and_dilation_rate(
    num_spatial_dims, strides, dilation_rate)

self.input_shape = input_shape
self.filter_shape = filter_shape
self.data_format = data_format
self.strides = strides
self.padding = padding
self.name = name
self.dilation_rate = dilation_rate
self.num_batch_dims = num_batch_dims
self.num_spatial_dims = num_spatial_dims
self.conv_op = _WithSpaceToBatch(
    input_shape,
    dilation_rate=dilation_rate,
    padding=padding,
    build_op=self._build_op,
    filter_shape=filter_shape,
    spatial_dims=spatial_dims,
    data_format=data_format,
    num_batch_dims=num_batch_dims)
