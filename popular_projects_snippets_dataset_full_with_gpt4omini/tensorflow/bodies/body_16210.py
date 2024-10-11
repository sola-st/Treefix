# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns a copy of `self` with `values` replaced by `new_value`.

    Preserves cached row-partitioning tensors such as `self.cached_nrows` and
    `self.cached_value_rowids` if they have values.

    Args:
      new_values: Potentially ragged tensor to use as the `values` for the
        returned `RaggedTensor`.  Must have `rank > 0`, and must have the same
        number of rows as `self.values`.

    Returns:
      A `RaggedTensor`.  `result.rank = 1 + new_values.rank`.
      `result.ragged_rank = 1 + new_values.ragged_rank`
    """
new_values = _convert_to_ragged_tensor_values(new_values)
new_values.shape.with_rank_at_least(1)
self.values.shape[:1].assert_is_compatible_with(new_values.shape[:1])
if (isinstance(new_values, RaggedTensor) and
    self._row_partition.dtype != new_values.row_splits.dtype):
    if not ragged_config.auto_cast_partition_dtype():
        raise ValueError("self and new_values have mismatched row_splits "
                         "dtypes; use RaggedTensor.with_row_splits_dtype() to "
                         "convert them to compatible dtypes.")
    new_values = new_values.with_row_splits_dtype(dtypes.int64)
    exit(self.with_row_splits_dtype(dtypes.int64).with_values(new_values))
exit(RaggedTensor(
    values=new_values, row_partition=self._row_partition, internal=True))
