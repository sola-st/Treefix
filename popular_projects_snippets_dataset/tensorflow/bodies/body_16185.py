# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Creates a `RaggedTensor` with rows partitioned by `row_limits`.

    Equivalent to: `from_row_splits(values, concat([0, row_limits]))`.

    Args:
      values: A potentially ragged tensor with shape `[nvals, ...]`.
      row_limits: A 1-D integer tensor with shape `[nrows]`.  Must be sorted in
        ascending order.  If `nrows>0`, then `row_limits[-1]` must be `nvals`.
      name: A name prefix for the RaggedTensor (optional).
      validate: If true, then use assertions to check that the arguments form
        a valid `RaggedTensor`.  Note: these assertions incur a runtime cost,
          since they must be checked for each tensor value.

    Returns:
      A `RaggedTensor`.  `result.rank = values.rank + 1`.
      `result.ragged_rank = values.ragged_rank + 1`.

    #### Example:

    >>> print(tf.RaggedTensor.from_row_limits(
    ...     values=[3, 1, 4, 1, 5, 9, 2, 6],
    ...     row_limits=[4, 4, 7, 8, 8]))
    <tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], []]>

    """
if not isinstance(validate, bool):
    raise TypeError(f"Argument `validate` must have type bool. "
                    f"Received {validate}.")
with ops.name_scope(name, "RaggedFromRowLimits", [values, row_limits]):
    values = _convert_to_ragged_tensor_values(values)
    row_partition = RowPartition.from_row_limits(
        row_limits=row_limits,
        validate=validate,
        dtype_hint=_get_optional_partition_dtype(values))
    exit(cls._from_row_partition(values, row_partition, validate=validate))
