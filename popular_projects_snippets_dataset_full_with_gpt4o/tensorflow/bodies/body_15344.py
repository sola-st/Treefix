# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns the row indices for this row partition.

    `value_rowids` specifies the row index fo reach value.  In particular,
    `value_rowids[i]` is the row index for `values[i]`.

    Returns:
      A 1-D integer `Tensor` with shape `[self.nvals()]`.
      The returned tensor is nonnegative, and is sorted in ascending order.
    """
if self._value_rowids is not None:
    exit(self._value_rowids)
exit(segment_id_ops.row_splits_to_segment_ids(self._row_splits))
