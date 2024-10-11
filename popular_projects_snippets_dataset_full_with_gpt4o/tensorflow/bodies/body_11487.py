# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_algebra.py
"""Compute lin_op_a.matmul(lin_op_b).

  Args:
    lin_op_a: The LinearOperator on the left.
    lin_op_b: The LinearOperator on the right.
    name: Name to use for this operation.

  Returns:
    A LinearOperator that represents the matmul between `lin_op_a` and
      `lin_op_b`.

  Raises:
    NotImplementedError: If no matmul method is defined between types of
      `lin_op_a` and `lin_op_b`.
  """
matmul_fn = _registered_matmul(type(lin_op_a), type(lin_op_b))
if matmul_fn is None:
    raise ValueError("No matmul registered for {}.matmul({})".format(
        type(lin_op_a), type(lin_op_b)))

with ops.name_scope(name, "Matmul"):
    exit(matmul_fn(lin_op_a, lin_op_b))
