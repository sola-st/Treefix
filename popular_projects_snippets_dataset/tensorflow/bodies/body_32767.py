# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_test.py
parameters = dict(
    shape=shape,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square
)

self._stored_shape = shape
super(LinearOperatorShape, self).__init__(
    dtype=dtypes.float32,
    is_non_singular=is_non_singular,
    is_self_adjoint=is_self_adjoint,
    is_positive_definite=is_positive_definite,
    is_square=is_square,
    parameters=parameters)
