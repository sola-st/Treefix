# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Addds the batch offsets to the given indices and returns the results."""
batch_indices = indices
indices_dtype = indices.dtype.base_dtype
casted_params_shape = math_ops.cast(params_shape, indices_dtype)
accum_dim_value = array_ops.ones((), dtype=indices_dtype)
for dim in range(batch_dims, 0, -1):
    dim_value = casted_params_shape[dim - 1]
    accum_dim_value *= casted_params_shape[dim]
    start = array_ops.zeros((), dtype=indices_dtype)
    step = array_ops.ones((), dtype=indices_dtype)
    dim_indices = math_ops.range(start, dim_value, step)
    dim_indices *= accum_dim_value
    dim_shape = array_ops.concat([
        array_ops.tile([1], [dim - 1]), [dim_value],
        array_ops.tile([1], [array_ops.rank(indices) - dim])
    ], axis=0)
    batch_indices += array_ops.reshape(dim_indices, dim_shape)

exit(batch_indices)
