# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/linear_operator_composition_test.py
del ensure_self_adjoint_and_pd
shape = list(build_info.shape)

# Create 2 matrices/operators, A1, A2, which becomes A = A1 A2.
# Use inner dimension of 2.
k = 2
batch_shape = shape[:-2]
shape_1 = batch_shape + [shape[-2], k]
shape_2 = batch_shape + [k, shape[-1]]

# Ensure that the matrices are well-conditioned by generating
# random matrices whose singular values are close to 1.
# The reason to do this is because cond(AB) <= cond(A) * cond(B).
# By ensuring that each factor has condition number close to 1, we ensure
# that the condition number of the product isn't too far away from 1.
def generate_well_conditioned(shape, dtype):
    m, n = shape[-2], shape[-1]
    min_dim = min(m, n)
    # Generate singular values that are close to 1.
    d = linear_operator_test_util.random_normal(
        shape[:-2] + [min_dim],
        mean=1.,
        stddev=0.1,
        dtype=dtype)
    zeros = array_ops.zeros(shape=shape[:-2] + [m, n], dtype=dtype)
    d = linalg_lib.set_diag(zeros, d)
    u, _ = linalg_lib.qr(linear_operator_test_util.random_normal(
        shape[:-2] + [m, m], dtype=dtype))

    v, _ = linalg_lib.qr(linear_operator_test_util.random_normal(
        shape[:-2] + [n, n], dtype=dtype))
    exit(math_ops.matmul(u, math_ops.matmul(d, v)))

matrices = [
    generate_well_conditioned(shape_1, dtype=dtype),
    generate_well_conditioned(shape_2, dtype=dtype),
]

lin_op_matrices = matrices

if use_placeholder:
    lin_op_matrices = [
        array_ops.placeholder_with_default(
            matrix, shape=None) for matrix in matrices]

operator = linalg.LinearOperatorComposition(
    [linalg.LinearOperatorFullMatrix(l) for l in lin_op_matrices])

matmul_order_list = list(reversed(matrices))
mat = matmul_order_list[0]
for other_mat in matmul_order_list[1:]:
    mat = math_ops.matmul(other_mat, mat)

exit((operator, mat))
