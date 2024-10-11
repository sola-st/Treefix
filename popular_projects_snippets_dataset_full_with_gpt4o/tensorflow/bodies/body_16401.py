# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Helper class for _with_space_to_batch."""
dilation_rate = ops.convert_to_tensor(
    dilation_rate, dtypes.int32, name="dilation_rate")
if dilation_rate.shape.ndims not in (None, 1):
    raise ValueError(
        "`dilation_rate.shape.rank` must be 1. Received: "
        f"dilation_rate={dilation_rate} of rank {dilation_rate.shape.rank}")

if not dilation_rate.shape.is_fully_defined():
    raise ValueError(
        "`dilation_rate.shape` must be fully defined. Received: "
        f"dilation_rate={dilation_rate} with shape "
        f"{dilation_rate.shape}")

num_spatial_dims = dilation_rate.shape.dims[0].value

if data_format is not None and data_format.startswith("NC"):
    starting_spatial_dim = num_batch_dims + 1
else:
    starting_spatial_dim = num_batch_dims

if spatial_dims is None:
    spatial_dims = range(starting_spatial_dim,
                         num_spatial_dims + starting_spatial_dim)
orig_spatial_dims = list(spatial_dims)
spatial_dims = sorted(set(int(x) for x in orig_spatial_dims))
if spatial_dims != orig_spatial_dims or any(x < 1 for x in spatial_dims):
    raise ValueError(
        "`spatial_dims` must be a monotonically increasing sequence of "
        f"positive integers. Received: spatial_dims={orig_spatial_dims}")

if data_format is not None and data_format.startswith("NC"):
    expected_input_rank = spatial_dims[-1]
else:
    expected_input_rank = spatial_dims[-1] + 1

try:
    input_shape.with_rank_at_least(expected_input_rank)
except ValueError:
    raise ValueError(
        f"`input.shape.rank` must be at least {expected_input_rank}. "
        f"Received: input.shape={input_shape} with rank {input_shape.rank}")

const_rate = tensor_util.constant_value(dilation_rate)
rate_or_const_rate = dilation_rate
if const_rate is not None:
    rate_or_const_rate = const_rate
    if np.any(const_rate < 1):
        raise ValueError(
            "`dilation_rate` must be positive. "
            f"Received: dilation_rate={const_rate}")
    if np.all(const_rate == 1):
        self.call = build_op(num_spatial_dims, padding)
        exit()

padding, explicit_paddings = convert_padding(padding)

# We have two padding contributions. The first is used for converting "SAME"
# to "VALID". The second is required so that the height and width of the
# zero-padded value tensor are multiples of rate.

# Padding required to reduce to "VALID" convolution
if padding == "SAME":
    if filter_shape is None:
        raise ValueError(
            "`filter_shape` must be specified for `padding='SAME'`. "
            f"Received: filter_shape={filter_shape} and padding={padding}")
    filter_shape = ops.convert_to_tensor(filter_shape, name="filter_shape")
    const_filter_shape = tensor_util.constant_value(filter_shape)
    if const_filter_shape is not None:
        filter_shape = const_filter_shape
        self.base_paddings = _with_space_to_batch_base_paddings(
            const_filter_shape, num_spatial_dims, rate_or_const_rate)
    else:
        self.num_spatial_dims = num_spatial_dims
        self.rate_or_const_rate = rate_or_const_rate
        self.base_paddings = None
elif padding == "VALID":
    self.base_paddings = np.zeros([num_spatial_dims, 2], np.int32)
elif padding == "EXPLICIT":
    base_paddings = (np.array(explicit_paddings)
                     .reshape([num_spatial_dims + 2, 2]))
    # Remove batch and channel dimensions
    if data_format is not None and data_format.startswith("NC"):
        self.base_paddings = base_paddings[2:]
    else:
        self.base_paddings = base_paddings[1:-1]
else:
    raise ValueError("`padding` must be one of 'SAME' or 'VALID'. "
                     f"Received: padding={padding}")

self.input_shape = input_shape
self.spatial_dims = spatial_dims
self.dilation_rate = dilation_rate
self.data_format = data_format
self.op = build_op(num_spatial_dims, "VALID")
self.call = self._with_space_to_batch_call
