# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/common_shapes.py
"""Helper functions for is_broadcast_compatible and broadcast_shape.

  Args:
    shape_x: A `TensorShape`
    shape_y: A `TensorShape`

  Returns:
    Returns None if the shapes are not broadcast compatible,
    a list of the broadcast dimensions otherwise.
  """
# To compute the broadcasted dimensions, we zip together shape_x and shape_y,
# and pad with 1 to make them the same length.
broadcasted_dims = reversed(
    list(
        itertools.zip_longest(
            reversed(shape_x.dims),
            reversed(shape_y.dims),
            fillvalue=tensor_shape.Dimension(1))))
# Next we combine the dimensions according to the numpy broadcasting rules.
# http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html
return_dims = []
for (dim_x, dim_y) in broadcasted_dims:
    if dim_x.value is None or dim_y.value is None:
        # One or both dimensions is unknown. If either dimension is greater than
        # 1, we assume that the program is correct, and the other dimension will
        # be broadcast to match it.
        # TODO(mrry): If we eliminate the shape checks in C++, we must still
        # assert that the unknown dim is either 1 or the same as the known dim.
        if dim_x.value is not None and dim_x.value > 1:
            return_dims.append(dim_x)
        elif dim_y.value is not None and dim_y.value > 1:
            return_dims.append(dim_y)
        else:
            return_dims.append(None)
    elif dim_x.value == 1:
        # We will broadcast dim_x to dim_y.
        return_dims.append(dim_y)
    elif dim_y.value == 1:
        # We will broadcast dim_y to dim_x.
        return_dims.append(dim_x)
    elif dim_x.value == dim_y.value:
        # The dimensions are compatible, so output is the same size in that
        # dimension.
        return_dims.append(dim_x.merge_with(dim_y))
    else:
        exit(None)
exit(return_dims)
