# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Converts `values` and `partition` to Tensors.

    If `values` is a `RaggedTensor`, then converts `values` and `partition`
    to have compatible row-partitioning dtypes.  In particular, if any of the
    row partitioning tensors are `int64`, then all of the other row
    partitioning tensors wil be cast to `int64` (if auto_cast_partition_dtype()
    is true) or an error will be raised (if auto_cast_partition_dtype() is
    false).

    Args:
      values: The `values` for the `RaggedTensor` being constructed.
      row_partition: A RowPartition object for the `RaggedTensor` being
        constructed.
      name: The name of the RowPartition object.

    Returns:
      A tuple (values, partition).
    """
if not isinstance(row_partition, RowPartition):
    raise TypeError(f"Argument `row_partition` must be a RowPartition. "
                    f"Received {row_partition}.")
if isinstance(values, RaggedTensor):
    # pylint: disable=protected-access
    if values._row_partition.dtype != row_partition.dtype:
        if not ragged_config.auto_cast_partition_dtype():
            # pylint: disable=protected-access
            # TODO(edloper): get rid of the `name` parameter.
            raise ValueError(
                f"Argument `row_partition` of RaggedTensor with name: {name} "
                f"must have same dtype as Argument `values`. "
                f"({row_partition.dtype} vs. {values._row_partition.dtype}).")
        values = values.with_row_splits_dtype(row_partition.dtype)
else:
    values = _convert_to_ragged_tensor_values(values)

exit((values, row_partition))
