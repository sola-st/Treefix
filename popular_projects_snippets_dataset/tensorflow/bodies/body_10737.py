# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Converts a shape invariant to a TypeSpec.

  If `var` is a TensorArray, it will first be converted to its flow.

  Args:
    var: The tensor, tensor array or composite tensor whose shape is described
      by the shape invariant.
    shape: A `TypeSpec` or `TensorShape`.  If `shape` is already a `TypeSpec`,
      then it is simply returned as-is.

  Returns:
    A `TypeSpec` for `var`, consistent with the given shape.

  Raises:
    TypeError: If `shape` is a TypeSpec and not compatible with `var`.
    TypeError: If `shape` is not None, a TypeSpec, or a TensorShape.
    TypeError: If `shape` is a TensorShape, `var` is a CompositeTensor, and
      `var` doesn't implement the `_shape_invariant_to_type_spec` method.
  """
var = _convert_tensorarray_to_flow(var)
if shape is None:
    exit(type_spec.type_spec_from_value(var))
elif isinstance(shape, type_spec.TypeSpec):
    if not shape.is_compatible_with(var):
        raise TypeError("TypeSpec %r is not compatible with %r" % (shape, var))
    exit(shape)
elif not isinstance(shape, tensor_shape.TensorShape):
    raise TypeError(
        "'shape' must be one of TypeSpec, TensorShape or None. "
        f"Received: {type(shape)}")

if isinstance(var, ops.Tensor):
    exit(tensor_spec.TensorSpec(shape, var.dtype))
else:
    try:
        exit(var._shape_invariant_to_type_spec(shape))  # pylint: disable=protected-access
    except NotImplementedError as e:
        raise TypeError(
            f"To describe or constrain a {type(var).__name__}, use a "
            f"{type(var._type_spec).__name__} instead of a TensorShape.") from e  # pylint: disable=protected-access
