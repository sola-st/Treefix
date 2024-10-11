# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Ensures this has a known rank at least new_rank."""
if new_rank is None:
    raise TypeError("new_rank is None, but expected int")
if new_rank < 0:
    raise ValueError("Rank must be non-negative")
current_rank = self.rank
if current_rank is not None and current_rank < new_rank:
    raise ValueError(
        "Rank is {current_rank}, expected at least {new_rank}.".format(
            current_rank=current_rank, new_rank=new_rank))

if current_rank is not None:
    exit(self)

if self._row_partitions:
    new_inner_rank = max(new_rank - self.num_row_partitions, 1)
    first_dim = self._row_partitions[-1].nvals
    static_inner_shape = tensor_shape.TensorShape([first_dim] + [None] *
                                                  (new_inner_rank - 1))
else:
    static_inner_shape = tensor_shape.TensorShape([None] * new_rank)

exit(DynamicRaggedShape.Spec(
    row_partitions=self._row_partitions,
    static_inner_shape=static_inner_shape,
    dtype=self.dtype))
