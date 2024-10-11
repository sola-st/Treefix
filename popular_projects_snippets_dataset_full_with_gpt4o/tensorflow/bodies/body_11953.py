# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/inverse_registrations.py
# Inverse decomposition of a Kronecker product is the Kronecker product
# of inverse decompositions.
exit(linear_operator_kronecker.LinearOperatorKronecker(
    operators=[
        operator.inverse() for operator in kronecker_operator.operators],
    is_non_singular=kronecker_operator.is_non_singular,
    is_self_adjoint=kronecker_operator.is_self_adjoint,
    is_positive_definite=kronecker_operator.is_positive_definite,
    is_square=True))
