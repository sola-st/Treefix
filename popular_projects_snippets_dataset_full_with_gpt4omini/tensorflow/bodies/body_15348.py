# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns the start indices for rows in this row partition.

    These indices specify where the values for each row begin.
    `partition.row_starts()` is equal to `partition.row_splits()[:-1]`.

    Returns:
      A 1-D integer Tensor with shape `[self.nrows()]`.
      The returned tensor is nonnegative, and is sorted in ascending order.
      `self.row_starts()[0] == 0`.
      `self.row_starts()[-1] <= self.nvals()`.
    """
exit(self._row_splits[:-1])
