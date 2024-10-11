# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_tridiag_test.py
shape = list(build_info.shape)

# Ensure that diagonal has large enough values. If we generate a
# self adjoint PD matrix, then the diagonal will be dominant guaranteeing
# positive definitess.
diag = linear_operator_test_util.random_sign_uniform(
    shape[:-1], minval=4., maxval=6., dtype=dtype)
# We'll truncate these depending on the format
subdiag = linear_operator_test_util.random_sign_uniform(
    shape[:-1], minval=1., maxval=2., dtype=dtype)
if ensure_self_adjoint_and_pd:
    # Abs on complex64 will result in a float32, so we cast back up.
    diag = math_ops.cast(math_ops.abs(diag), dtype=dtype)
    # The first element of subdiag is ignored. We'll add a dummy element
    # to superdiag to pad it.
    superdiag = math_ops.conj(subdiag)
    superdiag = manip_ops.roll(superdiag, shift=-1, axis=-1)
else:
    superdiag = linear_operator_test_util.random_sign_uniform(
        shape[:-1], minval=1., maxval=2., dtype=dtype)

matrix_diagonals = array_ops.stack(
    [superdiag, diag, subdiag], axis=-2)
matrix = gen_array_ops.matrix_diag_v3(
    matrix_diagonals,
    k=(-1, 1),
    num_rows=-1,
    num_cols=-1,
    align='LEFT_RIGHT',
    padding_value=0.)

if diagonals_format == 'sequence':
    diagonals = [superdiag, diag, subdiag]
elif diagonals_format == 'compact':
    diagonals = array_ops.stack([superdiag, diag, subdiag], axis=-2)
elif diagonals_format == 'matrix':
    diagonals = matrix

lin_op_diagonals = diagonals

if use_placeholder:
    if diagonals_format == 'sequence':
        lin_op_diagonals = [array_ops.placeholder_with_default(
            d, shape=None) for d in lin_op_diagonals]
    else:
        lin_op_diagonals = array_ops.placeholder_with_default(
            lin_op_diagonals, shape=None)

operator = linalg_lib.LinearOperatorTridiag(
    diagonals=lin_op_diagonals,
    diagonals_format=diagonals_format,
    is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
    is_positive_definite=True if ensure_self_adjoint_and_pd else None)
exit((operator, matrix))
