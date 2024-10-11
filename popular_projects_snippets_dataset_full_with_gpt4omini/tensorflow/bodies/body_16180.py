# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Creates a `RaggedTensor` with a row partition.

    This is used as a way for RaggedTensors to share row partitions.

    The outer dimension of values must be equal to `partition.nvals()`.

    Args:
      values: A potentially ragged tensor.
      row_partition: a `RowPartition`: can be shared between tensors.
      validate: If true, then use assertions to check that the arguments form a
        valid `RaggedTensor`.

    Returns:
      A `RaggedTensor`.  `result.rank = values.rank + 1`.
      `result.ragged_rank = values.ragged_rank + 1`.

    Raises:
      ValueError: If partition.nvals() != _nrows(values)
    """
if not isinstance(row_partition, RowPartition):
    raise TypeError(f"Argument `row_partition` must be a RowPartition. "
                    f"Received {row_partition}.")
if not isinstance(validate, bool):
    raise TypeError(f"Argument `validate` must have type bool. "
                    f"Received {validate}.")
values, row_partition = cls._convert_values_and_partition(
    values, row_partition, "partition")
if row_partition._has_precomputed_value_rowids():  # pylint: disable=protected-access
    value_rowids_shape = row_partition.value_rowids().shape
    values.shape[:1].assert_is_compatible_with(value_rowids_shape)
if validate:
    msg = "Arguments to _from_row_partition do not form a valid RaggedTensor"
    nvals = _nrows(values, row_partition.dtype)
    checks = [
        check_ops.assert_equal(
            math_ops.cast(row_partition.nvals(), row_partition.dtype),
            nvals,
            message=msg),
    ]
    if not isinstance(values, RaggedTensor):
        checks.append(check_ops.assert_rank_at_least(values, 1))
    row_partition = row_partition._with_dependencies(checks)  # pylint: disable=protected-access
exit(cls(values=values, internal=True, row_partition=row_partition))
