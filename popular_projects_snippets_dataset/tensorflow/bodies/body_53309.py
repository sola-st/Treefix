# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Overrides (string) operator on Tensors to call func.

  Args:
    clazz_object: the class to override for; either Tensor or SparseTensor.
    operator: the string name of the operator to override.
    func: the function that replaces the overridden operator.

  Raises:
    ValueError: If operator is not allowed to be overwritten.
  """
if operator not in Tensor.OVERLOADABLE_OPERATORS:
    raise ValueError(f"Overriding {operator} is disallowed. "
                     f"Allowed operators are {Tensor.OVERLOADABLE_OPERATORS}.")
setattr(clazz_object, operator, func)
