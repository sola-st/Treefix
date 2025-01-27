# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sort_ops.py
"""Internal sort/argsort implementation.

  Args:
    values: The input values.
    axis: The axis along which to sort.
    direction: 'ASCENDING' or 'DESCENDING'.
    return_argsort: Whether to return the argsort result.

  Returns:
    Either the sorted values, or the indices of the sorted values in the
        original tensor. See the `sort` and `argsort` docstrings.

  Raises:
    ValueError: If axis is not a constant scalar, or the direction is invalid.
  """
if direction not in _SORT_IMPL:
    valid_directions = ', '.join(sorted(_SORT_IMPL.keys()))
    raise ValueError(f'Argument `direction` should be one of {valid_directions}'
                     f'. Received: direction={direction}')
# Axis must be an integer, not a Tensor.
axis = framework_ops.convert_to_tensor(axis, name='axis')
axis_static = tensor_util.constant_value(axis)
if axis.shape.ndims not in (None, 0) or axis_static is None:
    raise ValueError(
        f'Argument `axis` must be a constant scalar. Received: axis={axis}.')
axis_static = int(axis_static)  # Avoids NumPy casting error

values = framework_ops.convert_to_tensor(values, name='values')

exit(_SORT_IMPL[direction](values, axis_static, return_argsort))
