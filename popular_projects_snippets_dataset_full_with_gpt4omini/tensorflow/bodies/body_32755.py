# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/matrix_solve_op_test.py
seed = [42, 24]
matrix_shape = [3, 3]
all_ops = []
for adjoint_ in False, True:
    lhs1 = stateless_random_ops.stateless_random_normal(
        matrix_shape, seed=seed)
    lhs2 = stateless_random_ops.stateless_random_normal(
        matrix_shape, seed=seed)
    rhs1 = stateless_random_ops.stateless_random_normal(
        matrix_shape, seed=seed)
    rhs2 = stateless_random_ops.stateless_random_normal(
        matrix_shape, seed=seed)
    s1 = linalg_ops.matrix_solve(lhs1, rhs1, adjoint=adjoint_)
    s2 = linalg_ops.matrix_solve(lhs2, rhs2, adjoint=adjoint_)
    all_ops += [s1, s2]
val = self.evaluate(all_ops)
for i in range(0, len(all_ops), 2):
    self.assertAllEqual(val[i], val[i + 1])
