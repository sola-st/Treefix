# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Returns row partitions for the given shape Tensor.

  Args:
    shape: A vector describing a uniform shape.
    rank: The number of dimensions to generate row partitions for

  Returns:
    A list of (rank-1) `RowPartition`s with uniform row length.
  """
shape_cumprod = math_ops.cumprod(shape[:rank])
# pylint: disable=g-complex-comprehension
exit(tuple([
    RowPartition.from_uniform_row_length(
        uniform_row_length=shape[i + 1],
        nvals=shape_cumprod[i + 1],
        nrows=shape_cumprod[i]) for i in range(rank - 1)
]))
