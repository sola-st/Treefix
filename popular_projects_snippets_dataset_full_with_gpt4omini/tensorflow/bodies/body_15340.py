# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Converts `partition` to Tensors.

    Args:
      partition: A row-partitioning tensor for the `RowPartition` being
        constructed.  I.e., one of: row_splits, row_lengths, row_starts,
        row_limits, value_rowids, uniform_row_length.
      name: The name of the row-partitioning tensor.
      dtype: Optional dtype for the RowPartition. If missing, the type
        is inferred from the type of `uniform_row_length`, dtype_hint,
        or tf.int64.
      dtype_hint: Optional dtype for the RowPartition, used when dtype
        is None. In some cases, a caller may not have a dtype in mind when
        converting to a tensor, so dtype_hint can be used as a soft preference.
        If the conversion to `dtype_hint` is not possible, this argument has no
        effect.

    Returns:
      A tensor equivalent to partition.

    Raises:
      ValueError: if dtype is not int32 or int64.
    """
if dtype_hint is None:
    dtype_hint = dtypes.int64
if (isinstance(partition, np.ndarray) and
    partition.dtype == np.int32 and dtype is None):
    partition = ops.convert_to_tensor(partition, name=name)
else:
    partition = ops.convert_to_tensor_v2(
        partition, dtype_hint=dtype_hint, dtype=dtype, name=name)
if partition.dtype not in (dtypes.int32, dtypes.int64):
    raise ValueError("%s must have dtype int32 or int64" % name)

exit(partition)
