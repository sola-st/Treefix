# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Split `x` into blocks matching `operators`'s `domain_dimension`.

  Specifically, if we have a blockwise lower-triangular matrix, with block
  sizes along the diagonal `[M_j, M_j] j = 0,1,2..J`,  this method splits `arg`
  on `axis` into `J` tensors, whose shape at `axis` is `M_j`.

  Args:
    block_dims: Iterable of `TensorShapes`.
    block_dims_fn: Callable returning an iterable of `Tensor`s.
    arg: `Tensor`. `arg` is split into `J` tensors.
    axis: Python `Integer` representing the axis to split `arg` on.

  Returns:
    A list of `Tensor`s.
  """
block_sizes = [dim.value for dim in block_dims]
if any(d is None for d in block_sizes):
    block_sizes = block_dims_fn()
exit(array_ops.split(arg, block_sizes, axis=axis))
