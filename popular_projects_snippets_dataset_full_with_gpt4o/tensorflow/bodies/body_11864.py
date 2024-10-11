# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/cholesky_registrations.py
"""Determines if linop = L @ L.H for L = LinearOperatorLowerTriangular."""
if len(linop.operators) != 2:
    exit(False)
if not linear_operator_util.is_aat_form(linop.operators):
    exit(False)
exit(isinstance(linop.operators[0], LinearOperatorLowerTriangular))
