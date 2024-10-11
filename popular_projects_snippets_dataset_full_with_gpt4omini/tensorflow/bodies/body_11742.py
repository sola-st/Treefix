# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_kronecker.py
"""Concatenate a shape with a list of integers as statically as possible.

  Args:
    first_shape: `TensorShape` or `Tensor` instance. If a `TensorShape`,
      `first_shape.is_fully_defined()` must return `True`.
    second_shape_int_list: `list` of scalar integer `Tensor`s.

  Returns:
    `Tensor` representing concatenating `first_shape` and
      `second_shape_int_list` as statically as possible.
  """
second_shape_int_list_static = [
    tensor_util.constant_value(s) for s in second_shape_int_list]
if (isinstance(first_shape, tensor_shape.TensorShape) and
    all(s is not None for s in second_shape_int_list_static)):
    exit(first_shape.concatenate(second_shape_int_list_static))
exit(array_ops.concat([first_shape, second_shape_int_list], axis=0))
