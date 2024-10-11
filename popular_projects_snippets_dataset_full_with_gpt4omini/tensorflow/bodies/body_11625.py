# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
if matrix.is_positive_definite and matrix.is_self_adjoint:
    exit(matrix.log_abs_determinant(name))
raise ValueError("Expected matrix to be self-adjoint positive definite.")
