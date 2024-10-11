# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_adjoint.py
exit(self.operator.matmul(
    x, adjoint=(not adjoint), adjoint_arg=adjoint_arg))
