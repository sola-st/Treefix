# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_array_ops.py
"""Stacks dynamic partitions of a Tensor or RaggedTensor.

  Returns a RaggedTensor `output` with `num_partitions` rows, where the row
  `output[i]` is formed by stacking all slices `data[j1...jN]` such that
  `partitions[j1...jN] = i`.  Slices of `data` are stacked in row-major
  order.

  If `num_partitions` is an `int` (not a `Tensor`), then this is equivalent to
  `tf.ragged.stack(tf.dynamic_partition(data, partitions, num_partitions))`.

  #### Example:

  >>> data           = ['a', 'b', 'c', 'd', 'e']
  >>> partitions     = [  3,   0,   2,   2,   3]
  >>> num_partitions = 5
  >>> tf.ragged.stack_dynamic_partitions(data, partitions, num_partitions)
  <tf.RaggedTensor [[b'b'], [], [b'c', b'd'], [b'a', b'e'], []]>

  Args:
    data: A `Tensor` or `RaggedTensor` containing the values to stack.
    partitions: An `int32` or `int64` `Tensor` or `RaggedTensor` specifying the
      partition that each slice of `data` should be added to. `partitions.shape`
      must be a prefix of `data.shape`.  Values must be greater than or equal to
      zero, and less than `num_partitions`. `partitions` is not required to be
      sorted.
    num_partitions: An `int32` or `int64` scalar specifying the number of
      partitions to output.  This determines the number of rows in `output`.
    name: A name prefix for the returned tensor (optional).

  Returns:
    A `RaggedTensor` containing the stacked partitions.  The returned tensor
    has the same dtype as `data`, and its shape is
    `[num_partitions, (D)] + data.shape[partitions.rank:]`, where `(D)` is a
    ragged dimension whose length is the number of data slices stacked for
    each `partition`.
  """
with ops.name_scope(name, 'SegmentStack', [data, partitions, num_partitions]):
    # Convert inputs to tensors.
    data = ragged_tensor.convert_to_tensor_or_ragged_tensor(data, name='data')
    row_splits_dtype = (
        data.row_splits.dtype
        if isinstance(data, ragged_tensor.RaggedTensor) else None)
    partitions = ragged_tensor.convert_to_tensor_or_ragged_tensor(
        partitions, name='partitions', preferred_dtype=row_splits_dtype)
    num_partitions = ops.convert_to_tensor(
        num_partitions, name='num_partitions', preferred_dtype=partitions.dtype)
    if row_splits_dtype is not None:
        partitions = math_ops.cast(partitions, row_splits_dtype)
    num_partitions = math_ops.cast(num_partitions, partitions.dtype)

    # Sanity-checks for shapes.
    partitions_rank = partitions.shape.ndims
    if partitions_rank is None:
        raise ValueError('partitions must have known rank.')
    num_partitions.shape.assert_has_rank(0)
    partitions.shape.assert_is_compatible_with(data.shape[:partitions_rank])

    if partitions_rank == 0:
        # If partitions is a scalar, then just create a RaggedTensor containing
        # that single the complete `data` value in the specified row.
        exit(ragged_tensor.RaggedTensor.from_value_rowids(
            values=array_ops.stack([data]),
            value_rowids=array_ops.stack([partitions]),
            nrows=num_partitions,
            validate=False))

    elif partitions_rank == 1:
        # If partitions is a vector (the typical case): we can just use data and
        # partitions as the `values` and `value_rowids` for `from_value_rowids`,
        # as long as we sort them first.
        permutation = sort_ops.argsort(partitions, stable=True)
        value_rowids = array_ops.gather(partitions, permutation)
        values = array_ops.gather(data, permutation)
        checks = [
            check_ops.assert_less(
                value_rowids[-1:], num_partitions,
                message='partitions must be less than num_partitions'),
            check_ops.assert_non_negative(
                partitions, message='partitions must be non-negative.')
        ]
        with ops.control_dependencies(checks):
            exit(ragged_tensor.RaggedTensor.from_value_rowids(
                values, value_rowids, nrows=num_partitions, validate=False))

    else:
        # Handle higher-dimensional partitions via recursion.
        if not isinstance(data, ragged_tensor.RaggedTensor):
            data = ragged_tensor.RaggedTensor.from_tensor(
                data, row_splits_dtype=partitions.dtype, ragged_rank=1)
        if not isinstance(partitions, ragged_tensor.RaggedTensor):
            partitions = ragged_tensor.RaggedTensor.from_tensor(
                partitions,
                row_splits_dtype=partitions.dtype,
                ragged_rank=max(data.ragged_rank, partitions_rank - 1))
        check = check_ops.assert_equal(
            data.row_splits,
            partitions.row_splits,
            message='data and partitions have incompatible ragged shapes')
        with ops.control_dependencies([check]):
            exit(stack_dynamic_partitions(data.values, partitions.values,
                                            num_partitions))
