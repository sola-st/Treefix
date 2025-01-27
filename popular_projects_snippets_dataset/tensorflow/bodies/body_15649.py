# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_batch_gather_with_default_op.py
"""Gets the RaggedTensorDynamicShape for the pad tensor."""
num_batch_dimensions = indices.shape.ndims - 1
params_shape = ragged_tensor_shape.RaggedTensorDynamicShape.from_tensor(
    params, dim_size_dtype=row_splits_dtype)

# We want to create a pad tensor that can be concatenated with the params.
if params.shape.ndims == indices.shape.ndims:
    # When params and indices are the same rank, the shape of the pad tensor is
    # almost identical to params, except the last dimension which has size = 1.
    if params_shape.num_inner_dimensions == 0:
        pad_dims = params_shape.partitioned_dim_sizes[:-1] + (
            array_ops.ones_like(params_shape.partitioned_dim_sizes[-1]),)
        exit(ragged_tensor_shape.RaggedTensorDynamicShape(
            pad_dims, []))
    else:
        exit(ragged_tensor_shape.RaggedTensorDynamicShape(
            params_shape.partitioned_dim_sizes,
            array_ops.concat([params_shape.inner_dim_sizes[:-1], [1]], axis=0)))
else:
    # When the rank of indices < params, the pad has the same dimension as
    # params up to the 'num_batch_dimensions' rank. Every dimension after that
    # has size 1.
    pad_dims = None
    if num_batch_dimensions == 0:
        pad_dims = (constant_op.constant(1, dtype=row_splits_dtype),) + (
            constant_op.constant([1], dtype=row_splits_dtype),) * (
                params_shape.num_partitioned_dimensions -
                num_batch_dimensions - 1)
    else:
        batch_dimensions = params_shape.partitioned_dim_sizes[
            :num_batch_dimensions]
        gather_dimension = params_shape.partitioned_dim_sizes[
            num_batch_dimensions]
        pad_dims = batch_dimensions + (
            array_ops.ones_like(gather_dimension),) * (
                params_shape.num_partitioned_dimensions - num_batch_dimensions)

    exit(ragged_tensor_shape.RaggedTensorDynamicShape(
        pad_dims, params_shape.inner_dim_sizes))
