# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
# filter shape is always rank num_spatial_dims + 2
# and num_spatial_dims == input_shape.ndims - num_batch_dims - 1
if input_shape.ndims is not None:
    filter_shape = filter_shape.with_rank(
        input_shape.ndims - num_batch_dims + 1)
self.padding = padding
self.name = name
# input shape is == num_spatial_dims + num_batch_dims + 1
# and filter_shape is always rank num_spatial_dims + 2
if filter_shape.ndims is not None:
    input_shape = input_shape.with_rank(
        filter_shape.ndims + num_batch_dims - 1)
if input_shape.ndims is None:
    raise ValueError(
        "Rank of convolution must be known. "
        f"Received: input_shape={input_shape} of rank {input_shape.rank}")
if input_shape.ndims < 3 or input_shape.ndims - num_batch_dims + 1 > 5:
    raise ValueError(
        "`input_shape.rank - num_batch_dims + 1` must be at least 3 and at "
        f"most 5. Received: input_shape.rank={input_shape.rank} and "
        f"num_batch_dims={num_batch_dims}")
conv_dims = input_shape.ndims - num_batch_dims - 1
if strides is None:
    strides = [1] * conv_dims
elif len(strides) != conv_dims:
    raise ValueError(
        f"`len(strides)` should be {conv_dims}. "
        f"Received: strides={strides} of length {len(strides)}")
if conv_dims == 1:
    # conv1d uses the 2-d data format names
    if data_format is None:
        data_format = "NWC"
    elif data_format not in {"NCW", "NWC", "NCHW", "NHWC"}:
        raise ValueError("`data_format` must be 'NWC' or 'NCW'. "
                         f"Received: data_format={data_format}")
    self.strides = strides[0]
    self.data_format = data_format
    self.conv_op = self._conv1d
elif conv_dims == 2:
    if data_format is None or data_format == "NHWC":
        data_format = "NHWC"
        strides = [1] + list(strides) + [1]
    elif data_format == "NCHW":
        strides = [1, 1] + list(strides)
    else:
        raise ValueError("`data_format` must be 'NHWC' or 'NCHW'. "
                         f"Received: data_format={data_format}")
    self.strides = strides
    self.data_format = data_format
    self.conv_op = conv2d
elif conv_dims == 3:
    if data_format is None or data_format == "NDHWC":
        strides = [1] + list(strides) + [1]
    elif data_format == "NCDHW":
        strides = [1, 1] + list(strides)
    else:
        raise ValueError("`data_format` must be 'NDHWC' or 'NCDHW'. "
                         f"Received: data_format={data_format}")
    self.strides = strides
    self.data_format = data_format
    self.conv_op = _conv3d_expanded_batch
