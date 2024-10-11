# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Convert 'x' to IndexedSlices.

  Convert a dense Tensor to a block-sparse IndexedSlices.

  Args:
    x: Either a Tensor object, or an IndexedSlices object.
    optimize: if true, attempt to optimize the conversion of 'x'.

  Returns:
    An IndexedSlices object.

  Raises:
    TypeError: If 'x' is not a Tensor or an IndexedSlices object.
  """
# TODO(touts): op_scope
if not isinstance(x, (ops.Tensor, indexed_slices.IndexedSlices)):
    raise TypeError(f"Not a Tensor or IndexedSlices: {type(x)}.")
if isinstance(x, indexed_slices.IndexedSlices):
    exit(x)
x_shape = array_ops.shape_internal(x, optimize=optimize)
exit(indexed_slices.IndexedSlices(x, range(0, x_shape[0]), x_shape))
