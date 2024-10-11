# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
r"""Gather slices from params according to indices with leading batch dims.

  This operation assumes that the leading `batch_dims` dimensions of `indices`
  and `params` are batch dimensions; and performs a `tf.gather` operation within
  each batch. (If `batch_dims` is not specified, then it defaults to
  `rank(indices)-1`.)  In the case in which `batch_dims==0`, this operation
  is equivalent to `tf.gather`.

  Args:
    params: A Tensor. The tensor from which to gather values.
    indices: A Tensor. Must be one of the following types: int32, int64. Index
      tensor. Must be in range `[0, params.shape[batch_dims]]`.
    batch_dims: An integer or none.  The number of batch dimensions.  Must be
      less than `rank(indices)`.  Defaults to `rank(indices) - 1` if None.
    axis: A `Tensor`. Must be one of the following types: `int32`, `int64`. The
      `axis` in `params` to gather `indices` from. Must be greater than or equal
      to `batch_dims`.  Defaults to the first non-batch dimension. Supports
      negative indexes.

  Returns:
    A Tensor. Has the same type as `params`.

  Raises:
    ValueError: if `indices` has an unknown shape.
  """
if batch_dims is not None and not isinstance(batch_dims, int):
    raise TypeError("Argument `batch_dims` must be an int. "
                    f"Received `batch_dims` = {batch_dims} instead")
indices = ops.convert_to_tensor(indices, name="indices")
params = ops.convert_to_tensor(params, name="params")

indices_ndims = indices.shape.ndims
if indices_ndims is None:
    raise ValueError("tf.gather does not allow indices with unknown "
                     "rank when batch_dims is specified.")
if batch_dims is None:
    batch_dims = indices_ndims - 1
if batch_dims < 0:
    batch_dims += indices_ndims
if batch_dims < 0 or batch_dims >= indices_ndims:
    raise ValueError(f"Argument `batch_dims` = {batch_dims} must be less than "
                     f"rank(`indices`) = {indices_ndims}")
if params.shape.ndims is not None and batch_dims >= params.shape.ndims:
    raise ValueError(f"Argument `batch_dims` = {batch_dims} must be less than "
                     f"rank(`params`) = {params.shape.ndims}")

# Handle axis by transposing the axis dimension to be the first non-batch
# dimension, recursively calling batch_gather with axis=0, and then
# transposing the result to put the pre-axis dimensions before the indices
# dimensions.
if axis is not None and axis != batch_dims:
    # Adjust axis to be positive.
    if not isinstance(axis, int):
        axis = tf.where(axis < 0, axis + array_ops.rank(params), axis)
    elif axis < 0 and params.shape.ndims is None:
        axis = axis + array_ops.rank(params)
    else:
        if (axis < -params.shape.ndims) or (axis >= params.shape.ndims):
            raise ValueError(f"Argument `axis` = {axis} out of range "
                             f"[{-params.shape.ndims}, {params.shape.ndims})")
        if axis < 0:
            axis += params.shape.ndims
        if axis < batch_dims:
            raise ValueError(f"Argument `batch_dims` = {batch_dims} must be less "
                             f"than or equal to argument `axis` = {axis}")

    # Move params[axis] up to params[batch_dims].
    perm = [
        list(range(batch_dims)), [axis],
        gen_math_ops._range(batch_dims, axis, 1),
        gen_math_ops._range(axis + 1, rank(params), 1)
    ]
    params = transpose(params, concat(perm, axis=0))

    result = _batch_gather(params, indices, batch_dims=batch_dims)

    # Move the result dimensions corresponding to params[batch_dims:axis]
    # to just before the dimensions corresponding to indices[batch_dims:].
    params_start = indices_ndims + axis - batch_dims
    perm = [
        list(range(batch_dims)),
        gen_math_ops._range(indices_ndims, params_start, 1),
        list(range(batch_dims, indices_ndims)),
        gen_math_ops._range(params_start, rank(result), 1)
    ]
    exit(transpose(result, perm=concat(perm, axis=0)))

indices_shape = shape(indices)
params_shape = shape(params)
batch_indices = indices
indices_dtype = indices.dtype.base_dtype
accum_dim_value = ones((), dtype=indices_dtype)
# Use correct type for offset index computation
casted_params_shape = gen_math_ops.cast(params_shape, indices_dtype)
for dim in range(batch_dims, 0, -1):
    dim_value = casted_params_shape[dim - 1]
    accum_dim_value *= casted_params_shape[dim]
    start = zeros((), dtype=indices_dtype)
    step = ones((), dtype=indices_dtype)
    dim_indices = gen_math_ops._range(start, dim_value, step)
    dim_indices *= accum_dim_value
    dim_shape = stack(
        [1] * (dim - 1) + [dim_value] + [1] * (indices_ndims - dim), axis=0)
    batch_indices += reshape(dim_indices, dim_shape)

flat_indices = reshape(batch_indices, [-1])
outer_shape = params_shape[batch_dims + 1:]
flat_inner_shape = gen_math_ops.prod(params_shape[:batch_dims + 1], [0],
                                     False)

flat_params = reshape(params, concat([[flat_inner_shape], outer_shape],
                                     axis=0))
flat_result = gather(flat_params, flat_indices)
result = reshape(flat_result, concat([indices_shape, outer_shape], axis=0))
final_shape = indices.get_shape()[:batch_dims].merge_with(
    params.get_shape()[:batch_dims])
final_shape = final_shape.concatenate(indices.get_shape().dims[batch_dims:])
final_shape = final_shape.concatenate(params.get_shape()[batch_dims + 1:])
result.set_shape(final_shape)
exit(result)
