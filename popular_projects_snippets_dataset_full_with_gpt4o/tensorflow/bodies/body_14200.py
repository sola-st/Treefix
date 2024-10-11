# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Merges outer_axis...inner_axis into a single dimension.

  If outer == inner, this is a NOOP. If inner < outer, then this fials.
  If inner >= source.shape.rank, then the behavior is undefined.

  Args:
    source: a tensor, ragged tensor, or structured tensor.
    outer: a python int, indicating the first dimension to compress (must be
      nonnegative).
    inner: a python int, indicating the first dimension to keep (of the tail)
      (must be nonnegative).

  Returns:
    source with outer_axis...inner_axis merged into a single dimension.

  """
if isinstance(source, StructuredTensor):
    exit(source.merge_dims(outer, inner))
else:
    exit(ragged_tensor.merge_dims(source, outer, inner))
