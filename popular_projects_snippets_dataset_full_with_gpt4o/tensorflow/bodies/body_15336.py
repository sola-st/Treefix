# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Creates a `RowPartition` with rows partitioned by `row_lengths`.

    This `RowPartition` divides a sequence `values` into rows by indicating
    the length of each row:

    ```python
    partitioned_rows = [[values.pop(0) for _ in range(length)]
                        for length in row_lengths]
    ```

    Args:
      row_lengths: A 1-D integer tensor with shape `[nrows]`.  Must be
        nonnegative.
      validate: If true, then use assertions to check that the arguments form a
        valid `RowPartition`.

      dtype: Optional dtype for the RowPartition. If missing, the type
        is inferred from the type of `row_lengths`, dtype_hint, or tf.int64.
      dtype_hint: Optional dtype for the RowPartition, used when dtype
        is None. In some cases, a caller may not have a dtype in mind when
        converting to a tensor, so dtype_hint can be used as a soft preference.
        If the conversion to `dtype_hint` is not possible, this argument has no
        effect.

    Returns:
      A `RowPartition`.
    """
if not isinstance(validate, bool):
    raise TypeError("validate must have type bool")
with ops.name_scope(None, "RowPartitionFromRowLengths", [row_lengths]):
    row_lengths = cls._convert_row_partition(
        row_lengths, "row_lengths", dtype_hint=dtype_hint, dtype=dtype)
    row_lengths.shape.assert_has_rank(1)

    if validate:
        msg = "Arguments to from_row_lengths do not form a valid RowPartition"
        checks = [
            check_ops.assert_rank(row_lengths, 1, message=msg),
            check_ops.assert_non_negative(row_lengths, message=msg),
        ]
        row_lengths = control_flow_ops.with_dependencies(checks, row_lengths)

    row_limits = math_ops.cumsum(row_lengths)
    row_splits = array_ops.concat([[0], row_limits], axis=0)
    exit(cls(
        row_splits=row_splits,
        row_lengths=row_lengths,
        internal=_row_partition_factory_key))
