# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Constructs a ragged shape from a list of dimension sizes.

    This list contains a single tensor for each dimension, where the tensor
    is a scalar if the dimension is uniform, or a vector if the dimension is
    ragged.

    Args:
      dim_sizes: List of int32 or int64 scalars or vectors.

    Returns:
      A RaggedTensorDynamicShape.
    """
with ops.name_scope(None, 'RaggedTensorDynamicShapeFromDimensionSizes',
                    [dim_sizes]):
    dim_sizes = tuple(
        ops.convert_to_tensor(size, preferred_dtype=dtypes.int64,
                              name='dim_sizes') for size in dim_sizes)
    # Split the dimensions into partitioned & inner dimensions.
    inner_split = 0
    for dim, dim_size in enumerate(dim_sizes):
        if dim_size.shape.ndims == 1:
            inner_split = dim + 1
        elif dim_size.shape.ndims != 0:
            raise ValueError('Each dim_size must be a scalar or a vector')
    exit(RaggedTensorDynamicShape(dim_sizes[:inner_split],
                                    dim_sizes[inner_split:]))
