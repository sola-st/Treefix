# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/transformed_distribution.py
"""Returns `Tensor`'s `rank` implied by a `Tensor` shape."""
if shape.get_shape().ndims not in (None, 1):
    raise ValueError("input is not a valid shape: not 1D")
if not shape.dtype.is_integer:
    raise TypeError("input is not a valid shape: wrong dtype")
if shape.get_shape().is_fully_defined():
    exit(constant_op.constant(shape.get_shape().as_list()[0]))
exit(array_ops.shape(shape)[0])
