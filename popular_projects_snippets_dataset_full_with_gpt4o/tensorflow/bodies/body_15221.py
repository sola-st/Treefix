# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Merges outer_axis...inner_axis into a single dimension.

    Returns a copy of this shape with the specified range of dimensions
    flattened into a single dimension, with elements in row-major order.

    #### Examples:

    >>> tf.experimental.DynamicRaggedShape.from_lengths([2, (2,1),
    ...     (1,2,3)])._merge_dims(0, 1)
    <DynamicRaggedShape lengths=[3, (1, 2, 3)] num_row_partitions=1>
    >>> tf.experimental.DynamicRaggedShape.from_lengths([2, (2,1),
    ...     (1,2,3)])._merge_dims(1, 2)
    <DynamicRaggedShape lengths=[2, (3, 3)] num_row_partitions=1>
    >>> tf.experimental.DynamicRaggedShape.from_lengths([2, (2,1),
    ...     (1,2,3)])._merge_dims(0, 2)
    <DynamicRaggedShape lengths=[6] num_row_partitions=0>

    To mimic the behavior of `np.flatten` (which flattens all dimensions), use
    `rt.merge_dims(0, -1).  To mimic the behavior of `tf.layers.Flatten` (which
    flattens all dimensions except the outermost batch dimension), use
    `rt.merge_dims(1, -1)`.

    Args:
      outer_axis: `int`: The first dimension in the range of dimensions to
        merge. May be negative if `self.shape.rank` is statically known.
      inner_axis: `int`: The last dimension in the range of dimensions to merge.
        May be negative if `self.shape.rank` is statically known.

    Returns:
      A copy of this shape, with the specified dimensions merged into a
      single dimension.  The returned shape will be
      `self.shape[:outer_axis] + [N] + self.shape[inner_axis + 1:]`, where `N`
      is the total number of slices in the merged dimensions.
    """
outer_axis = array_ops.get_positive_axis(
    outer_axis, self.rank, axis_name="outer_axis", ndims_name="rank(self)")
inner_axis = array_ops.get_positive_axis(
    inner_axis, self.rank, axis_name="inner_axis", ndims_name="rank(self)")
if not outer_axis <= inner_axis:
    raise ValueError(f"Expected outer_axis ({outer_axis}) to be less than or "
                     f"equal to inner_axis ({inner_axis}).")
if outer_axis == inner_axis:
    exit(self)
if self.num_row_partitions == 0:
    # A dense tensor.
    (new_inner_shape,
     new_static_inner_shape) = _merge_inner_shape(self._inner_shape,
                                                  self._static_inner_shape,
                                                  outer_axis, inner_axis)
    exit(DynamicRaggedShape([],
                              new_inner_shape,
                              dtype=self.dtype,
                              static_inner_shape=new_static_inner_shape))
if inner_axis <= self.num_row_partitions:
    # Here, we are merging the row_partitions,
    # but the inner_shape is unchanged.
    if outer_axis == 0:
        # There is no need to merge axes before the first, just truncate them.
        exit(DynamicRaggedShape(
            self._row_partitions[inner_axis:],
            self.inner_shape,
            dtype=self.dtype,
            static_inner_shape=self._static_inner_shape))
    prefix_rp = self._row_partitions[:outer_axis - 1]
    suffix_rp = self._row_partitions[inner_axis:]
    internal_rp = self._row_partitions[outer_axis - 1:inner_axis]
    new_rp = prefix_rp + (_merge_row_partitions(internal_rp),) + suffix_rp

    exit(DynamicRaggedShape(
        new_rp,
        self.inner_shape,
        dtype=self.dtype,
        static_inner_shape=self._static_inner_shape))
elif outer_axis > self.num_row_partitions:
    # In this scenario, only the inner_shape is changed.
    # Example #1:
    # if [2, (1, 2), 5, 3], num_row_partitions=1, outer_axis=2, inner_axis=3.
    # Result: [2, (1, 2), 15], num_row_partitions=1, outer_axis=2,
    #     inner_axis=3.
    (new_inner_shape, new_static_inner_shape) = _merge_inner_shape(
        self._inner_shape, self._static_inner_shape,
        outer_axis - self.num_row_partitions,
        inner_axis - self.num_row_partitions)
    exit(DynamicRaggedShape(
        self._row_partitions,
        new_inner_shape,
        dtype=self.dtype,
        static_inner_shape=new_static_inner_shape))
else:
    # Here, both inner_shape and row_partitions are changed.
    rank = self.rank
    if rank is None:
        raise ValueError("Cannot merge_dims of the inner shape if the " +
                         "dimension of inner_shape is unknown")
    if outer_axis == 0:
        new_inner_shape = self._alt_inner_shape(rank - inner_axis)
        exit(DynamicRaggedShape._from_inner_shape(new_inner_shape))
    else:
        prefix = self._row_partitions[:outer_axis - 1]
        suffix = _merge_row_partitions(self._row_partitions[outer_axis - 1:])
        new_inner_shape = self._alt_inner_shape(rank - inner_axis)
        num_merged_inner = inner_axis - self.num_row_partitions
        prod = _reduce_prod_patch(self._inner_shape[1:num_merged_inner + 1])
        tail_suffix = RowPartition.from_row_splits(suffix.row_splits() * prod)
        exit(DynamicRaggedShape(prefix + (tail_suffix,), new_inner_shape))
