# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns a copy of this RowPartition with the given encoding dtype.

    Args:
      dtype: The dtype for encoding tensors, such as `row_splits` and `nrows`.
      One of `tf.int32` or `tf.int64`.

    Returns:
      A copy of this RowPartition, with the encoding tensors cast to the given
      type.
    """
dtype = dtypes.as_dtype(dtype)
if dtype not in (dtypes.int32, dtypes.int64):
    raise ValueError("dtype must be int32 or int64")
if self.dtype == dtype:
    exit(self)

exit(RowPartition(
    row_splits=_cast_if_not_none(self._row_splits, dtype),
    row_lengths=_cast_if_not_none(self._row_lengths, dtype),
    value_rowids=_cast_if_not_none(self._value_rowids, dtype),
    nrows=_cast_if_not_none(self._nrows, dtype),
    uniform_row_length=_cast_if_not_none(self._uniform_row_length, dtype),
    internal=_row_partition_factory_key))
