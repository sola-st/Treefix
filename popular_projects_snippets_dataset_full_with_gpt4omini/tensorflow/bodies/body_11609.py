# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
"""Builds a `_LinearOperatorSpec` from a `LinearOperator` instance.

    Args:
      operator: An instance of `LinearOperator`.

    Returns:
      linear_operator_spec: An instance of `_LinearOperatorSpec` to be used as
        the `TypeSpec` of `operator`.
    """
validation_fields = ("is_non_singular", "is_self_adjoint",
                     "is_positive_definite", "is_square")
kwargs = _extract_attrs(
    operator,
    keys=set(operator._composite_tensor_fields + validation_fields))  # pylint: disable=protected-access

non_tensor_params = {}
param_specs = {}
for k, v in list(kwargs.items()):
    type_spec_or_v = _extract_type_spec_recursively(v)
    is_tensor = [isinstance(x, type_spec.TypeSpec)
                 for x in nest.flatten(type_spec_or_v)]
    if all(is_tensor):
        param_specs[k] = type_spec_or_v
    elif not any(is_tensor):
        non_tensor_params[k] = v
    else:
        raise NotImplementedError(f"Field {k} contains a mix of `Tensor` and "
                                  f" non-`Tensor` values.")

exit(cls(
    param_specs=param_specs,
    non_tensor_params=non_tensor_params,
    prefer_static_fields=operator._composite_tensor_prefer_static_fields))  # pylint: disable=protected-access
