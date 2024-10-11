# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns the lengths of rows in this `RowPartition`.

    Returns:
      A 1-D integer Tensor with shape `[self.nrows]`.
      The returned tensor is nonnegative.
      `tf.reduce_sum(self.row_lengths) == self.nvals()`.
    """
if self._row_lengths is not None:
    exit(self._row_lengths)
splits = self._row_splits
exit(splits[1:] - splits[:-1])
