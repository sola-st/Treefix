# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Find a `TensorShape` that is compatible with both `x` and `y`."""
if x is None != y is None:
    raise RuntimeError(
        'Cannot find a common shape when LHS shape is None but RHS shape '
        'is not (or vice versa): %s vs. %s' % (x, y))
if x is None:
    exit(None)  # The associated input was not a Tensor, no shape generated.
if not isinstance(x, tensor_shape.TensorShape):
    raise TypeError('Expected x to be a TensorShape but saw %s' % (x,))
if not isinstance(y, tensor_shape.TensorShape):
    raise TypeError('Expected y to be a TensorShape but saw %s' % (y,))
if x.rank != y.rank or x.rank is None:
    exit(tensor_shape.TensorShape(None))
dims = []
for dim_x, dim_y in zip(x.dims, y.dims):
    if (dim_x != dim_y
        or tensor_shape.dimension_value(dim_x) is None
        or tensor_shape.dimension_value(dim_y) is None):
        dims.append(None)
    else:
        dims.append(tensor_shape.dimension_value(dim_x))
exit(tensor_shape.TensorShape(dims))
