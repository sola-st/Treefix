# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/adjoint_registrations.py
  # Adjoint of a Kronecker product is the Kronecker product
  # of adjoints.
exit(linear_operator_kronecker.LinearOperatorKronecker(
    operators=[
        operator.adjoint() for operator in kronecker_operator.operators],
    is_non_singular=kronecker_operator.is_non_singular,
    is_self_adjoint=kronecker_operator.is_self_adjoint,
    is_positive_definite=kronecker_operator.is_positive_definite,
    is_square=True))
