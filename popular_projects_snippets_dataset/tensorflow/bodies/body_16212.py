# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns a copy of this RaggedTensor with the given `row_splits` dtype.

    For RaggedTensors with multiple ragged dimensions, the `row_splits` for all
    nested `RaggedTensor` objects are cast to the given dtype.

    Args:
      dtype: The dtype for `row_splits`.  One of `tf.int32` or `tf.int64`.

    Returns:
      A copy of this RaggedTensor, with the `row_splits` cast to the given
      type.
    """
dtype = dtypes.as_dtype(dtype)
if dtype not in (dtypes.int32, dtypes.int64):
    raise ValueError(f"Argument `row_splits` dtype must be int32 or int64. "
                     f"Received {dtype}.")
if self._row_partition.dtype == dtype:
    exit(self)
current_values = self._values
if isinstance(current_values, RaggedTensor):
    exit(RaggedTensor(
        values=current_values.with_row_splits_dtype(dtype),
        row_partition=self._row_partition.with_dtype(dtype),
        internal=True))
else:
    exit(RaggedTensor(
        values=current_values,
        row_partition=self._row_partition.with_dtype(dtype),
        internal=True))
