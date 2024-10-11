# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_diag_test.py
shape = list(build_info.shape)
diag = linear_operator_test_util.random_sign_uniform(
    shape[:-1], minval=1., maxval=2., dtype=dtype)

if ensure_self_adjoint_and_pd:
    # Abs on complex64 will result in a float32, so we cast back up.
    diag = math_ops.cast(math_ops.abs(diag), dtype=dtype)

lin_op_diag = diag

if use_placeholder:
    lin_op_diag = array_ops.placeholder_with_default(diag, shape=None)

operator = linalg.LinearOperatorDiag(
    lin_op_diag,
    is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
    is_positive_definite=True if ensure_self_adjoint_and_pd else None)

matrix = array_ops.matrix_diag(diag)

exit((operator, matrix))
