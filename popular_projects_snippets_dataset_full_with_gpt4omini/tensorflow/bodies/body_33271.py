# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_zeros_test.py
del ensure_self_adjoint_and_pd
del use_placeholder
shape = list(build_info.shape)
assert shape[-1] == shape[-2]

batch_shape = shape[:-2]
num_rows = shape[-1]

operator = linalg_lib.LinearOperatorZeros(
    num_rows, batch_shape=batch_shape, dtype=dtype)
matrix = array_ops.zeros(shape=shape, dtype=dtype)

exit((operator, matrix))
