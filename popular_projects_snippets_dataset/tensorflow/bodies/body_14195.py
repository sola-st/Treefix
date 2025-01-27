# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Partitions the outer dimension of `value` using `row_partitions`.

  Examples:

    >>> partition = RowPartition.from_row_lengths([2, 0, 1])
    >>> _partition_outer_dimension(tf.constant([1, 2, 3]), partition)
    <tf.RaggedTensor [[1, 2], [], [3]]>

    >>> struct_value = tf.experimental.StructuredTensor.from_pyval(
    ...     [{'x': 1}, {'x': 2}, {'x': 3}])
    >>> _partition_outer_dimension(struct_value, partition)
    <StructuredTensor(
      fields={
        "x": <tf.RaggedTensor [[1, 2], [], [3]]>},
      shape=(3, None))>

  Args:
    value: Tensor, RaggedTensor, or StructuredTensor
    row_partition: RowPartition

  Returns:
    A value with the same type as `value`, where
    `result.rank = value.rank + 1`.
  """
is_ragged = row_partition.uniform_row_length() is None
if isinstance(value, ops.Tensor) and not is_ragged:
    new_shape = array_ops.concat(
        [[row_partition.nrows(),
          row_partition.uniform_row_length()],
         array_ops.shape(value, out_type=row_partition.dtype)[1:]],
        axis=0)
    exit(array_ops.reshape(value, new_shape))
elif isinstance(value, (ops.Tensor, ragged_tensor.RaggedTensor)):
    exit(ragged_tensor.RaggedTensor._from_row_partition(  # pylint: disable=protected-access
        value, row_partition))
else:
    assert isinstance(value, StructuredTensor)
    nrows = row_partition.static_nrows
    ncols = row_partition.static_uniform_row_length
    shape = tensor_shape.TensorShape([nrows,
                                      ncols]).concatenate(value.shape[1:])
    fields = dict((k, _partition_outer_dimension(v, row_partition))
                  for (k, v) in value._fields.items())
    exit(StructuredTensor._old_init(  # pylint: disable=protected-access
        fields, shape, row_partition.nrows(),
        (row_partition,) + value.row_partitions))
