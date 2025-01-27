# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_low_rank_update_test.py
# Recall A = L + UDV^H
shape = list(shape_info.shape)
diag_shape = shape[:-1]
k = shape[-2] // 2 + 1
u_perturbation_shape = shape[:-1] + [k]
diag_update_shape = shape[:-2] + [k]

# base_operator L will be a symmetric positive definite diagonal linear
# operator, with condition number as high as 1e4.
base_diag = self._gen_positive_diag(dtype, diag_shape)
lin_op_base_diag = base_diag

# U
u = linear_operator_test_util.random_normal_correlated_columns(
    u_perturbation_shape, dtype=dtype)
lin_op_u = u

# V
v = linear_operator_test_util.random_normal_correlated_columns(
    u_perturbation_shape, dtype=dtype)
lin_op_v = v

# D
if self._is_diag_update_positive or ensure_self_adjoint_and_pd:
    diag_update = self._gen_positive_diag(dtype, diag_update_shape)
else:
    diag_update = linear_operator_test_util.random_normal(
        diag_update_shape, stddev=1e-4, dtype=dtype)
lin_op_diag_update = diag_update

if use_placeholder:
    lin_op_base_diag = array_ops.placeholder_with_default(
        base_diag, shape=None)
    lin_op_u = array_ops.placeholder_with_default(u, shape=None)
    lin_op_v = array_ops.placeholder_with_default(v, shape=None)
    lin_op_diag_update = array_ops.placeholder_with_default(
        diag_update, shape=None)

base_operator = linalg.LinearOperatorDiag(
    lin_op_base_diag,
    is_positive_definite=True,
    is_self_adjoint=True)

operator = linalg.LinearOperatorLowRankUpdate(
    base_operator,
    lin_op_u,
    v=lin_op_v if self._use_v else None,
    diag_update=lin_op_diag_update if self._use_diag_update else None,
    is_diag_update_positive=self._is_diag_update_positive)

# The matrix representing L
base_diag_mat = array_ops.matrix_diag(base_diag)

# The matrix representing D
diag_update_mat = array_ops.matrix_diag(diag_update)

# Set up mat as some variant of A = L + UDV^H
if self._use_v and self._use_diag_update:
    # In this case, we have L + UDV^H and it isn't symmetric.
    expect_use_cholesky = False
    matrix = base_diag_mat + math_ops.matmul(
        u, math_ops.matmul(diag_update_mat, v, adjoint_b=True))
elif self._use_v:
    # In this case, we have L + UDV^H and it isn't symmetric.
    expect_use_cholesky = False
    matrix = base_diag_mat + math_ops.matmul(u, v, adjoint_b=True)
elif self._use_diag_update:
    # In this case, we have L + UDU^H, which is PD if D > 0, since L > 0.
    expect_use_cholesky = self._is_diag_update_positive
    matrix = base_diag_mat + math_ops.matmul(
        u, math_ops.matmul(diag_update_mat, u, adjoint_b=True))
else:
    # In this case, we have L + UU^H, which is PD since L > 0.
    expect_use_cholesky = True
    matrix = base_diag_mat + math_ops.matmul(u, u, adjoint_b=True)

if expect_use_cholesky:
    self.assertTrue(operator._use_cholesky)
else:
    self.assertFalse(operator._use_cholesky)

exit((operator, matrix))
