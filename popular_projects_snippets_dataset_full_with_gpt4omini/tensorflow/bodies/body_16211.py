# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
"""Returns a copy of `self` with `flat_values` replaced by `new_value`.

    Preserves cached row-partitioning tensors such as `self.cached_nrows` and
    `self.cached_value_rowids` if they have values.

    Args:
      new_values: Potentially ragged tensor that should replace
        `self.flat_values`.  Must have `rank > 0`, and must have the same number
        of rows as `self.flat_values`.

    Returns:
      A `RaggedTensor`.
      `result.rank = self.ragged_rank + new_values.rank`.
      `result.ragged_rank = self.ragged_rank + new_values.ragged_rank`.
    """
if isinstance(self._values, RaggedTensor):
    exit(self.with_values(self.values.with_flat_values(new_values)))
else:
    new_values = _convert_to_ragged_tensor_values(new_values)
exit(self.with_values(new_values))
