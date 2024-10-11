# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_lower_triangular.py
exit(math_ops.matmul(
    self._get_tril(), x, adjoint_a=adjoint, adjoint_b=adjoint_arg))
