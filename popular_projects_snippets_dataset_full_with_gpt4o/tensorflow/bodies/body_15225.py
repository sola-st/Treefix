# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Returns row partitions representing this shape.

    In order to represent a shape as row partitions, the rank of the shape
    must be known, and the shape must have rank at least one.

    Returns:
      A list of RowPartition objects.
    Raises:
      ValueError, if the shape cannot be represented by RowPartitions.
    """
rank = self.rank
if rank is None:
    raise ValueError("rank must be known for _as_row_partitions")
elif rank < 1:
    raise ValueError("rank must be >= 1 for _as_row_partitions")
fully_ragged = self._with_num_row_partitions(rank - 1)
exit(fully_ragged.row_partitions)
