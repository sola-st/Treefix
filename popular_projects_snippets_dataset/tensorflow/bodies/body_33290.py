# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
del use_placeholder
del ensure_self_adjoint_and_pd
shape = list(build_info.shape)

batch_shape = shape[:-2]
num_rows = shape[-2]
num_columns = shape[-1]

operator = linalg_lib.LinearOperatorZeros(
    num_rows, num_columns, is_square=False, is_self_adjoint=False,
    batch_shape=batch_shape, dtype=dtype)
matrix = array_ops.zeros(shape=shape, dtype=dtype)

exit((operator, matrix))
