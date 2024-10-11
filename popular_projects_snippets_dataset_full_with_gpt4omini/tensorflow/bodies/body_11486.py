# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_algebra.py
"""Get the Cholesky factor associated to lin_op_a.

  Args:
    lin_op_a: The LinearOperator to decompose.
    name: Name to use for this operation.

  Returns:
    A LinearOperator that represents the lower Cholesky factor of `lin_op_a`.

  Raises:
    NotImplementedError: If no Cholesky method is defined for the LinearOperator
      type of `lin_op_a`.
  """
cholesky_fn = _registered_cholesky(type(lin_op_a))
if cholesky_fn is None:
    raise ValueError("No cholesky decomposition registered for {}".format(
        type(lin_op_a)))

with ops.name_scope(name, "Cholesky"):
    exit(cholesky_fn(lin_op_a))
