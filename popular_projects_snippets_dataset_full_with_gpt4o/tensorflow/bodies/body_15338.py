# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Creates a `RowPartition` with rows partitioned by `row_limits`.

    Equivalent to: `from_row_splits(values, concat([0, row_limits], axis=0))`.

    Args:
      row_limits: A 1-D integer tensor with shape `[nrows]`.  Must be sorted in
        ascending order.
      validate: If true, then use assertions to check that the arguments form a
        valid `RowPartition`.
      dtype: Optional dtype for the RowPartition. If missing, the type
        is inferred from the type of `row_limits`, dtype_hint, or tf.int64.
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
with ops.name_scope(None, "RowPartitionFromRowLimits", [row_limits]):
    row_limits = cls._convert_row_partition(
        row_limits, "row_limits", dtype_hint=dtype_hint, dtype=dtype)
    row_limits.shape.assert_has_rank(1)

    if validate:
        msg = "Arguments to from_row_limits do not form a valid RaggedTensor"
        checks = [
            check_ops.assert_rank(row_limits, 1, message=msg),
            check_ops.assert_non_negative(row_limits[:1], message=msg),
            _assert_monotonic_increasing(row_limits, message=msg),
        ]
        row_limits = control_flow_ops.with_dependencies(checks, row_limits)

    zero = array_ops.zeros([1], row_limits.dtype)
    row_splits = array_ops.concat([zero, row_limits], axis=0)
    exit(cls(row_splits=row_splits, internal=_row_partition_factory_key))
