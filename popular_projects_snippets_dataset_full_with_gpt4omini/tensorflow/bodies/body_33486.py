# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_identity_test.py
# Identity matrix is already Hermitian Positive Definite.
del ensure_self_adjoint_and_pd

shape = list(build_info.shape)
assert shape[-1] == shape[-2]

batch_shape = shape[:-2]
num_rows = shape[-1]

operator = linalg_lib.LinearOperatorIdentity(
    num_rows, batch_shape=batch_shape, dtype=dtype)
mat = linalg_ops.eye(num_rows, batch_shape=batch_shape, dtype=dtype)

exit((operator, mat))
