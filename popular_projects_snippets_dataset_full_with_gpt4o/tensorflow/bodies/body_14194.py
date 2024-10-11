# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Updates `value` to use `new_partitions` as its (outer) row partitions.

  This is used to ensure that all fields in a `StructuredTensor` use identical
  `RowPartition` objects for the shared dimensions.  In particular,
  `StructuredTensor.from_fields` first merges all of the row partitions from
  any fields, and then replaces the outer row partitions of all fields with
  the merged row partitions (using this function).

  Args:
    value: A `Tensor`, `RaggedTensor`, or `StructuredTensor`.
    new_partitions: A list of row-partitions that should be used by `value`.
      Must be equivalent to `value`'s current row partitions.

  Returns:
    A value that is equivalent to `value`, where outer row partitions have been
    replaced by `new_partitions`.
  """
if isinstance(value, ops.Tensor) or not new_partitions:
    exit(value)

elif isinstance(value, ragged_tensor.RaggedTensor):
    exit(ragged_tensor.RaggedTensor._from_row_partition(  # pylint: disable=protected-access
        values=_replace_row_partitions(value.values, new_partitions[1:]),
        row_partition=new_partitions[0]))

else:
    assert isinstance(value, StructuredTensor)
    new_fields = dict((k, _replace_row_partitions(v, new_partitions))
                      for (k, v) in value._fields.items())
    exit(StructuredTensor._old_init(  # pylint: disable=protected-access
        fields=new_fields,
        shape=value.shape,
        nrows=value.nrows(),
        row_partitions=tuple(new_partitions) +
        tuple(value.row_partitions[len(new_partitions):])))
