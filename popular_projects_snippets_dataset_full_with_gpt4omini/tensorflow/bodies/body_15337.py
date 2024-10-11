# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Creates a `RowPartition` with rows partitioned by `row_starts`.

    Equivalent to: `from_row_splits(concat([row_starts, nvals], axis=0))`.

    Args:
      row_starts: A 1-D integer tensor with shape `[nrows]`.  Must be
        nonnegative and sorted in ascending order.  If `nrows>0`, then
        `row_starts[0]` must be zero.
      nvals: A scalar tensor indicating the number of values.
      validate: If true, then use assertions to check that the arguments form a
        valid `RowPartition`.
      dtype: Optional dtype for the RowPartition. If missing, the type
        is inferred from the type of `row_starts`, dtype_hint, or tf.int64.
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
with ops.name_scope(None, "RowPartitionFromRowStarts", [row_starts]):
    row_starts = cls._convert_row_partition(
        row_starts, "row_starts", dtype_hint=dtype_hint, dtype=dtype)
    row_starts.shape.assert_has_rank(1)
    # TODO(martinz): nvals and row_starts could be inconsistent at call time,
    # even though they eventually end up the same type.
    nvals = math_ops.cast(nvals, row_starts.dtype)
    if validate:
        msg = "Arguments to from_row_starts do not form a valid RaggedTensor"
        checks = [
            check_ops.assert_rank(row_starts, 1, message=msg),
            _assert_zero(row_starts[:1], message=msg),
            _assert_monotonic_increasing(row_starts, message=msg),
            check_ops.assert_less_equal(row_starts[-1:], nvals, message=msg),
        ]
        row_starts = control_flow_ops.with_dependencies(checks, row_starts)

    row_splits = array_ops.concat([row_starts, [nvals]], axis=0)
    exit(cls(row_splits=row_splits, nvals=nvals,
               internal=_row_partition_factory_key))
