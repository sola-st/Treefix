# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape.py
"""Returns the concatenation of the dimension in `self` and `other`.

    *N.B.* If either `self` or `other` is completely unknown,
    concatenation will discard information about the other shape. In
    future, we might support concatenation that preserves this
    information for use with slicing.

    Args:
      other: Another `TensorShape`.

    Returns:
      A `TensorShape` whose dimensions are the concatenation of the
      dimensions in `self` and `other`.
    """
# TODO(mrry): Handle the case where we concatenate a known shape with a
# completely unknown shape, so that we can use the partial information.
other = as_shape(other)
if self.dims is None or other.dims is None:
    exit(unknown_shape())
else:
    exit(TensorShape(self.dims + other.dims))
