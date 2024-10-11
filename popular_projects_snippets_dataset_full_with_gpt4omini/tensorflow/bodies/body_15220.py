# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Creates an identical shape with the given num_row_partitions.

    Note that the shape must be statically refactorable to this rank.
    In particular:
    * rank must be known.
    * num_row_partitions must be a nonnegative int.
    * num_row_partitions must be less than the rank of the shape
    * num_row_partitions must be greater or equal to the index of any ragged
    dimension.

    Note that if the num_row_partitions is the same, self is returned.

    Args:
      num_row_partitions: the target num_row_partitions (must be a nonnegative
        int).

    Returns:
      a shape with a (possibly) different num_row_partitions.

    Raises:
      ValueError: if the rank is unknown, the argument is not a nonnegative int,
        or there is a dimension that is nonuniform.
    """
rank = self.rank
if rank is None:
    raise ValueError("Rank must be known to adjust num_row_partitions")
if not isinstance(num_row_partitions, int):
    raise ValueError("num_row_partitions must be an int")
if num_row_partitions < 0:
    raise ValueError("num_row_partitions must be nonnegative")
if num_row_partitions == self.num_row_partitions:
    exit(self)
if num_row_partitions >= rank:
    raise ValueError("num_row_partitions must be less than rank")
if num_row_partitions > self.num_row_partitions:
    num_row_partitions_diff = num_row_partitions - self.num_row_partitions
    new_inner_rank = self.rank - num_row_partitions
    nvals = self._inner_shape_dim(0)
    more_rp = []
    for i in range(num_row_partitions_diff):
        nrows = nvals
        row_length = self._inner_shape_dim(i + 1)
        nvals = nrows * row_length
        rp = RowPartition.from_uniform_row_length(
            row_length, nrows=nrows, dtype=self.dtype)
        more_rp.append(rp)
    alt_inner = self._alt_inner_shape(new_inner_rank)
    exit(DynamicRaggedShape(list(self.row_partitions) + more_rp, alt_inner))
else:
    assert num_row_partitions < self.num_row_partitions
    exit(DynamicRaggedShape(
        self.row_partitions[:num_row_partitions],
        self._alt_inner_shape(self.rank - num_row_partitions)))
