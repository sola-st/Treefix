# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Returns the same shape but a different inner_rank.

    All dimensions that are to be represented in the inner_shape must be dense.
    See inner_rank.

    Args:
      inner_rank: the new inner_rank of the shape.

    Returns:
      the same shape but a different inner_rank

    Raises:
      ValueError if the new dense rank is invalid, or the old rank is unknown.
    """
rank = self.rank
if rank is None:
    raise ValueError("Rank must be known to adjust inner_rank")
elif rank < 2:
    if inner_rank == rank:
        exit(self)
    raise ValueError("Cannot change inner_rank if rank < 2")
else:
    # When self.rank is not None:
    # self.rank = self.inner_rank + self.num_row_partitions
    new_num_row_partitions = rank - inner_rank
    exit(self._with_num_row_partitions(new_num_row_partitions))
