# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Broadcasts rt_input to the ragged shape `dst_shape`."""
# Check that rt_input and dst_shape have the same row_splits dtype.
if (isinstance(rt_input, ragged_tensor.RaggedTensor) and
    rt_input.row_splits.dtype != dst_shape.dim_size_dtype):
    if not ragged_config.auto_cast_partition_dtype():
        raise ValueError('rt_input and dst_shape have different row_split '
                         'dtypes; use RaggedTensor.with_row_splits_dtype() or '
                         'RaggedTensorDynamicShape.with_dim_size_dtype() to '
                         'convert to a compatible dtype.')
    rt_input = rt_input.with_row_splits_dtype(dtypes.int64)
    dst_shape = dst_shape.with_dim_size_dtype(dtypes.int64)

# dst_shape's rank and ragged_rank must be greater than or equal to rt_input's
if rt_input.shape.ndims is None or dst_shape.rank is None:
    raise ValueError('Unable to broadcast: unknown rank')
if rt_input.shape.ndims > dst_shape.rank:
    raise ValueError('Incompatible with shape: rank mismatch')
if (isinstance(rt_input, ragged_tensor.RaggedTensor) and
    rt_input.ragged_rank >= dst_shape.num_partitioned_dimensions):
    raise ValueError('Incompatible with shape: ragged rank mismatch')

src_shape = RaggedTensorDynamicShape.from_tensor(rt_input)
src_shape = src_shape.broadcast_to_rank(dst_shape.rank)

# Add dimensions to rt_input so its rank and ragged_rank matches dst_shape.
if dst_shape.rank > rt_input.shape.ndims:
    if rt_input.shape.ndims < dst_shape.num_inner_dimensions + 1:
        rt_input = array_ops.reshape(
            rt_input, array_ops.concat([[-1], dst_shape.inner_dim_sizes], axis=0))
    for _ in range(dst_shape.rank - rt_input.shape.ndims):
        if ragged_tensor.is_ragged(rt_input):
            nrows = rt_input.nrows()
        else:
            nrows = array_ops.shape(rt_input,
                                    out_type=dst_shape.dim_size_dtype)[0]
        rt_input = ragged_tensor.RaggedTensor.from_row_lengths(rt_input, [nrows],
                                                               validate=False)

  # Add ragged dimensions to match dst_shape.
if ragged_tensor.is_ragged(rt_input):
    inner_rank_diff = (
        rt_input.flat_values.shape.ndims - 1 - dst_shape.num_inner_dimensions)
    if inner_rank_diff > 0:
        rt_input = rt_input.with_flat_values(
            ragged_tensor.RaggedTensor.from_tensor(
                rt_input.flat_values, ragged_rank=inner_rank_diff,
                row_splits_dtype=dst_shape.dim_size_dtype))
else:
    rt_input = ragged_tensor.RaggedTensor.from_tensor(
        rt_input, ragged_rank=dst_shape.num_partitioned_dimensions - 1,
        row_splits_dtype=dst_shape.dim_size_dtype)

# Do broadcasting for any dimensions that will remain uniform.  We can do
# these all at once, since they're independent of one another.
multiples = [1] * dst_shape.rank
for axis in range(dst_shape.num_partitioned_dimensions):
    if not src_shape.is_ragged(axis) and not dst_shape.is_ragged(axis):
        src_size = src_shape.dimension_size(axis)
        dst_size = dst_shape.dimension_size(axis)
        if ((tensor_util.constant_value(src_size) in (1, None)) and
            (tensor_util.constant_value(dst_size) != 1)):
            multiples[axis] = array_ops.where(
                math_ops.equal(src_size, 1), dst_size, 1)
if not all(isinstance(v, int) and v == 1 for v in multiples):
    multiples = array_ops.stack(multiples, axis=0)
    rt_input = ragged_array_ops.tile(rt_input, multiples)

if broadcast_inner_dimensions:
    new_shape = array_ops.broadcast_dynamic_shape(
        array_ops.shape(
            rt_input.flat_values, out_type=dst_shape.dim_size_dtype),
        array_ops.concat([[1], dst_shape.inner_dim_sizes], axis=0))
    rt_input = rt_input.with_flat_values(
        array_ops.broadcast_to(rt_input.flat_values, new_shape))

# Do broadcasting for dimensions that become ragged.  We must do these from
# outermost to innermost.
for axis in range(dst_shape.num_partitioned_dimensions):
    if not src_shape.is_ragged(axis) and dst_shape.is_ragged(axis):
        dst_size = dst_shape.dimension_size(axis)
        rt_input = _ragged_tile_axis(rt_input, axis, dst_size,
                                     dst_shape.dim_size_dtype)

exit(rt_input)
