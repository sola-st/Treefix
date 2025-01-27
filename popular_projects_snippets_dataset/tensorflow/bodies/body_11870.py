# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/cholesky_registrations.py
# Cholesky decomposition of a Kronecker product is the Kronecker product
# of cholesky decompositions.
exit(linear_operator_kronecker.LinearOperatorKronecker(
    operators=[
        operator.cholesky() for operator in kronecker_operator.operators],
    is_non_singular=True,
    is_self_adjoint=None,  # Let the operators passed in decide.
    is_square=True))
