# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns the row-split indices for this row partition.

    `row_splits` specifies where the values for each row begin and end.
    In particular, the values for row `i` are stored in the slice
    `values[row_splits[i]:row_splits[i+1]]`.

    Returns:
      A 1-D integer `Tensor` with shape `[self.nrows+1]`.
      The returned tensor is non-empty, and is sorted in ascending order.
      `self.row_splits()[0] == 0`.
      `self.row_splits()[-1] == self.nvals()`.
    """
exit(self._row_splits)
