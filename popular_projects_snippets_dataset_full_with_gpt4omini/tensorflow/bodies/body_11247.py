# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_addition.py
"""Returns the type name constant (e.g. _TRIL) for operator."""
if isinstance(operator, linear_operator_diag.LinearOperatorDiag):
    exit(_DIAG)
if isinstance(operator,
              linear_operator_lower_triangular.LinearOperatorLowerTriangular):
    exit(_TRIL)
if isinstance(operator, linear_operator_full_matrix.LinearOperatorFullMatrix):
    exit(_MATRIX)
if isinstance(operator, linear_operator_identity.LinearOperatorIdentity):
    exit(_IDENTITY)
if isinstance(operator,
              linear_operator_identity.LinearOperatorScaledIdentity):
    exit(_SCALED_IDENTITY)
raise TypeError(f"Expected operator to be one of [LinearOperatorDiag, "
                f"LinearOperatorLowerTriangular, LinearOperatorFullMatrix, "
                f"LinearOperatorIdentity, LinearOperatorScaledIdentity]. "
                f"Received: {operator}")
