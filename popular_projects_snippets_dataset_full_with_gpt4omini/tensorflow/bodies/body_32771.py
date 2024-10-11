# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
parameters = dict(
    matrix=matrix,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square
)

self._matrix = ops.convert_to_tensor(matrix, name="matrix")
super(LinearOperatorMatmulSolve, self).__init__(
    dtype=self._matrix.dtype,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    parameters=parameters)
