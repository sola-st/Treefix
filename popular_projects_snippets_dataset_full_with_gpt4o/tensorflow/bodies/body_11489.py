# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_algebra.py
"""Get the Inverse associated to lin_op_a.

  Args:
    lin_op_a: The LinearOperator to decompose.
    name: Name to use for this operation.

  Returns:
    A LinearOperator that represents the inverse of `lin_op_a`.

  Raises:
    NotImplementedError: If no Inverse method is defined for the LinearOperator
      type of `lin_op_a`.
  """
inverse_fn = _registered_inverse(type(lin_op_a))
if inverse_fn is None:
    raise ValueError("No inverse registered for {}".format(
        type(lin_op_a)))

with ops.name_scope(name, "Inverse"):
    exit(inverse_fn(lin_op_a))
