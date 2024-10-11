# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns the length of each row in this partition, if rows are uniform.

    If all rows in this `RowPartition` have the same length, then this returns
    that length as a scalar integer `Tensor`.  Otherwise, it returns `None`.

    Returns:
      scalar Tensor with `type=self.dtype`, or `None`.
    """
exit(self._uniform_row_length)
