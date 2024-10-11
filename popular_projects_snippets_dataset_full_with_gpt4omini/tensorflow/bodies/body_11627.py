# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
if not isinstance(matrix, LinearOperator):
    raise ValueError("Passing in `matrix` as a Tensor and `rhs` as a "
                     "LinearOperator is not supported.")
exit(matrix.solve(rhs, adjoint=adjoint, name=name))
