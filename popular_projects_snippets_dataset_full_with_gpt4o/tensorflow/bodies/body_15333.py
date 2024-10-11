# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Creates a `RowPartition` from the specified encoding tensor(s).

    This constructor is private -- please use one of the following ops to
    build `RowPartition`s:

      * `RowPartition.from_row_lengths`
      * `RowPartition.from_value_rowids`
      * `RowPartition.from_row_splits`
      * `RowPartition.from_row_starts`
      * `RowPartition.from_row_limits`
      * `RowPartition.from_uniform_row_length`

    If row_splits is has a constant value, then all other arguments should
    have a constant value.

    Args:
      row_splits: A 1-D integer tensor with shape `[nrows+1]`.
      row_lengths: A 1-D integer tensor with shape `[nrows]`
      value_rowids: A 1-D integer tensor with shape `[nvals]`.
      nrows: A 1-D integer scalar tensor.
      uniform_row_length: A scalar tensor.
      nvals: A scalar tensor.
      internal: Private key value, required to ensure that this private
        constructor is *only* called from the factory methods.

    Raises:
      TypeError: If a row partitioning tensor has an inappropriate dtype.
      TypeError: If exactly one row partitioning argument was not specified.
      ValueError: If a row partitioning tensor has an inappropriate shape.
      ValueError: If multiple partitioning arguments are specified.
      ValueError: If nrows is specified but value_rowids is not None.
    """
if internal is not _row_partition_factory_key:
    raise ValueError("RowPartition constructor is private; please use one "
                     "of the factory methods instead (e.g., "
                     "RowPartition.from_row_lengths())")

# Validate the arguments.
if not isinstance(row_splits, ops.Tensor):
    raise TypeError("Row-partitioning argument must be a Tensor, got %r" %
                    row_splits)
if row_splits.dtype not in (dtypes.int32, dtypes.int64):
    raise ValueError("Row-partitioning argument must be int32 or int64")

# Validate shapes & dtypes.
row_splits.shape.assert_has_rank(1)
row_splits.set_shape([None])
self._row_splits = row_splits

# Store any cached tensors.  These are used to avoid unnecessary
# round-trip conversions when a RowPartition is constructed from
# lengths or rowids, and we later want those lengths/rowids back.
for tensor in [row_lengths, value_rowids, nrows, uniform_row_length, nvals]:
    if tensor is not None:
        if not isinstance(tensor, ops.Tensor):
            raise TypeError("Cached value must be a Tensor or None.")
        elif tensor.dtype != row_splits.dtype:
            raise ValueError(f"Inconsistent dtype for encoding tensors: "
                             f"{tensor} vs {row_splits}")
self._row_lengths = row_lengths
self._value_rowids = value_rowids
self._nrows = nrows
self._uniform_row_length = uniform_row_length
self._nvals = nvals
