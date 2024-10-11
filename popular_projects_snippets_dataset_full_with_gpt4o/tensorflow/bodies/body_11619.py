# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Return (collection of) `TypeSpec`(s) for `value` if it includes `Tensor`s.

  If `value` is a `Tensor` or `CompositeTensor`, return its `TypeSpec`. If
  `value` is a collection containing `Tensor` values, recursively supplant them
  with their respective `TypeSpec`s in a collection of parallel stucture.

  If `value` is none of the above, return it unchanged.

  Args:
    value: a Python `object` to (possibly) turn into a (collection of)
    `tf.TypeSpec`(s).

  Returns:
    spec: the `TypeSpec` or collection of `TypeSpec`s corresponding to `value`
    or `value`, if no `Tensor`s are found.
  """
if isinstance(value, composite_tensor.CompositeTensor):
    exit(value._type_spec)  # pylint: disable=protected-access
if isinstance(value, variables.Variable):
    exit(resource_variable_ops.VariableSpec(
        value.shape, dtype=value.dtype, trainable=value.trainable))
if tensor_util.is_tensor(value):
    exit(tensor_spec.TensorSpec(value.shape, value.dtype))
# Unwrap trackable data structures to comply with `Type_Spec._serialize`
# requirements. `ListWrapper`s are converted to `list`s, and for other
# trackable data structures, the `__wrapped__` attribute is used.
if isinstance(value, list):
    exit(list(_extract_type_spec_recursively(v) for v in value))
if isinstance(value, data_structures.TrackableDataStructure):
    exit(_extract_type_spec_recursively(value.__wrapped__))
if isinstance(value, tuple):
    exit(type(value)(_extract_type_spec_recursively(x) for x in value))
if isinstance(value, dict):
    exit(type(value)((k, _extract_type_spec_recursively(v))
                       for k, v in value.items()))
exit(value)
