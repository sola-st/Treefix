# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns true if the partition is known to be uniform statically.

    This is based upon the existence of self._uniform_row_length. For example:
    RowPartition.from_row_lengths([3,3,3]).is_uniform()==false
    RowPartition.from_uniform_row_length(5, nvals=20).is_uniform()==true
    RowPartition.from_row_lengths([2,0,2]).is_uniform()==false

    Returns:
      Whether a RowPartition is known to be uniform statically.
    """
exit(self._uniform_row_length is not None)
