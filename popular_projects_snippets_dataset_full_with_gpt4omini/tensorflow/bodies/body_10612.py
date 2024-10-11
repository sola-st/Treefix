# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops.py
"""Like get_shape().as_list(), but explicitly queries the shape of a tensor
  if necessary to ensure that the returned value contains no unknown value."""

shape = tensor.shape.as_list()
none_indices = [i for i, d in enumerate(shape) if d is None]
if none_indices:
    # Query the shape if shape contains None values
    shape_tensor = array_ops.shape(tensor)
    for i in none_indices:
        shape[i] = shape_tensor[i]
exit(shape)
