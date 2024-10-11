# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_composition_test.py
shape = list(build_info.shape)

# Either 1 or 2 matrices, depending.
num_operators = rng.randint(low=1, high=3)
if ensure_self_adjoint_and_pd:
    # The random PD matrices are also symmetric. Here we are computing
    # A @ A ... @ A. Since A is symmetric and PD, so are any powers of it.
    matrices = [
        linear_operator_test_util.random_positive_definite_matrix(
            shape, dtype, force_well_conditioned=True)] * num_operators
else:
    matrices = [
        linear_operator_test_util.random_positive_definite_matrix(
            shape, dtype, force_well_conditioned=True)
        for _ in range(num_operators)
    ]

lin_op_matrices = matrices

if use_placeholder:
    lin_op_matrices = [
        array_ops.placeholder_with_default(
            matrix, shape=None) for matrix in matrices]

operator = linalg.LinearOperatorComposition(
    [linalg.LinearOperatorFullMatrix(l) for l in lin_op_matrices],
    is_positive_definite=True if ensure_self_adjoint_and_pd else None,
    is_self_adjoint=True if ensure_self_adjoint_and_pd else None,
    is_square=True)

matmul_order_list = list(reversed(matrices))
mat = matmul_order_list[0]
for other_mat in matmul_order_list[1:]:
    mat = math_ops.matmul(other_mat, mat)

exit((operator, mat))
