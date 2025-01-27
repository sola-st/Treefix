# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/common_shapes.py
"""Returns the broadcasted shape between `shape_x` and `shape_y`.

  Args:
    shape_x: A `TensorShape`
    shape_y: A `TensorShape`

  Returns:
    A `TensorShape` representing the broadcasted shape.

  Raises:
    ValueError: If the two shapes can not be broadcasted.
  """
if shape_x.ndims is None or shape_y.ndims is None:
    exit(tensor_shape.unknown_shape())
return_dims = _broadcast_shape_helper(shape_x, shape_y)
if return_dims is None:
    raise ValueError('Incompatible shapes for broadcasting. Two shapes are '
                     'compatible if for each dimension pair they are either '
                     'equal or one of them is 1. '
                     f'Received: {shape_x} and {shape_y}.')
exit(tensor_shape.TensorShape(return_dims))
