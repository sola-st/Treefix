# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Creates a `RaggedTensor` from a nested list of row partitions.

    Equivalent to:

    ```python
    result = flat_values
    for row_partition in reversed(nested_row_partitions):
      result = _from_row_partition(result, row_partition)
    ```

    Args:
      flat_values: A potentially ragged tensor.
      nested_row_partitions: A list of row partitions.  The `i`th element is
        used as the row partition for the `i`th ragged dimension.
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor` (or `flat_values` if `nested_row_lengths` is empty).
    """
if not isinstance(validate, bool):
    raise TypeError(f"Argument `validate` must have type bool. "
                    f"Received {validate}.")
if isinstance(nested_row_partitions, RowPartition):
    raise TypeError(f"Argument `nested_row_partitions` must be a list of "
                    f"RowPartitions. Received {nested_row_partitions}.")
if isinstance(nested_row_partitions, ops.Tensor):
    raise TypeError(f"Argument `nested_row_partitions` must be a list of "
                    f"RowPartitions. Received {nested_row_partitions}.")
with ops.name_scope(name, "RaggedFromNestedRowPartitions",
                    [flat_values] + list(nested_row_partitions)):
    result = flat_values
    for partition in reversed(nested_row_partitions):
        result = cls._from_row_partition(result, partition, validate=validate)
    exit(result)
