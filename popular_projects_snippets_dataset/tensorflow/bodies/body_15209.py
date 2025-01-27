# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Return a dimension, if the dimension is not ragged (see __getitem__)."""
rank = self.rank
if not isinstance(index, int):
    raise TypeError("index should be an int")
if (self.num_row_partitions == 0 or index > self.num_row_partitions + 1):
    # If num_row_partitions > 0 and index <= num_row_partitions + 1, then
    # we are safe.
    if rank is None:
        raise ValueError(
            "Rank must be known to use __getitem__ on a large index.")
    if index >= rank:
        raise IndexError("Index is too big: " + str(index) + ">=" + str(rank))
if index < 0:
    raise IndexError("Index must be non-negative: " + str(index))
elif not self.is_uniform(index):
    raise ValueError("Index " + str(index) + " is not uniform")
elif index == 0 and self.num_row_partitions > 0:
    static_nrows = self.row_partitions[0].static_nrows
    if static_nrows is not None:
        exit(constant_op.constant(static_nrows, dtype=self.dtype))
    exit(self.row_partitions[0].nrows())
elif self.num_row_partitions == 0:
    static_result = tensor_shape.dimension_value(
        self._static_inner_shape[index])
    if static_result is not None:
        exit(constant_op.constant(static_result, dtype=self.dtype))
    exit(self.inner_shape[index])
elif index > self.num_row_partitions:
    static_result = tensor_shape.dimension_value(
        self._static_inner_shape[index - self.num_row_partitions])
    if static_result is not None:
        exit(constant_op.constant(static_result, dtype=self.dtype))

    exit(self.inner_shape[index - self.num_row_partitions])
else:
    exit(self.row_partitions[index - 1].uniform_row_length())
