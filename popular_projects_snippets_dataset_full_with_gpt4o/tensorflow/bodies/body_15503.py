# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor_shape.py
"""Creates a RaggedTensorDynamicShape.

    Args:
      partitioned_dim_sizes: A `list` of 0-D or 1-D integer `Tensor`, one for
        each partitioned dimension.  If dimension `d` is uniform, then
        `partitioned_dim_sizes[d]` must be an integer scalar, specifying the
        size of all slices across dimension `d`.  If dimension `d` is ragged,
        then `partitioned_dim_sizes[d]` must be an integer vector, specifying
        the size of each slice across dimension `d`.
      inner_dim_sizes: A 1-D integer `Tensor`, whose length is equal to the
        number of inner dimensions.  `inner_dim_sizes[n]` is the size of all
        slices across the `n`th inner dimension (which is the
        `(len(partitioned_dim_sizes)+n)`th dimension in the overall tensor.
      dim_size_dtype: dtype for dimension sizes.  If not specified, then it
        is chosen based on the dtypes of `partitioned_dim_sizes` and
        `inner_dim_sizes`.
    """
assert isinstance(partitioned_dim_sizes, (list, tuple))

with ops.name_scope(None, 'RaggedTensorDynamicShape',
                    (partitioned_dim_sizes, inner_dim_sizes)):
    partitioned_dim_sizes = tuple(
        ops.convert_to_tensor(size, name='partitioned_dimension_size_%d' % i)
        for (i, size) in enumerate(partitioned_dim_sizes))
    inner_dim_sizes = ops.convert_to_tensor(
        inner_dim_sizes, name='inner_dim_sizes')

    # Validate shapes.
    if partitioned_dim_sizes:
        for axis, dimension_size in enumerate(partitioned_dim_sizes):
            if dimension_size.shape.ndims is None:
                raise ValueError(
                    'rank of partitioned_dim_sizes[%d] is unknown' % axis)
            dimension_size.shape.with_rank_at_most(1)
        if partitioned_dim_sizes[0].shape.ndims == 1:
            raise ValueError('outermost partitioned dimension must be uniform')
        if partitioned_dim_sizes[-1].shape.ndims == 0:
            raise ValueError('innermost partitioned dimension must be ragged')
    inner_dim_sizes.shape.assert_has_rank(1)

    # Convert dimension size tensors to a single dtype.
    if dim_size_dtype is None:
        dim_size_dtypes = set(
            p.dtype for p in partitioned_dim_sizes if p.shape.ndims == 1)
        if not dim_size_dtypes:
            dim_size_dtype = dtypes.int64
        elif len(dim_size_dtypes) == 1:
            dim_size_dtype = dim_size_dtypes.pop()
        else:
            if not ragged_config.auto_cast_partition_dtype():
                raise ValueError('partitioned_dim_sizes must have matching dtypes')
            dim_size_dtype = dtypes.int64
    partitioned_dim_sizes = tuple(math_ops.cast(p, dim_size_dtype)
                                  for p in partitioned_dim_sizes)
    inner_dim_sizes = math_ops.cast(inner_dim_sizes, dim_size_dtype)

    self._partitioned_dim_sizes = partitioned_dim_sizes
    self._inner_dim_sizes = inner_dim_sizes
