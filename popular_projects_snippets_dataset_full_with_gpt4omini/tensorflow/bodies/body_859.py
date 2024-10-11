# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_solve_op_test.py
with self.session() as sess:
    lhs1 = random_ops.random_normal([3, 3], seed=42)
    lhs2 = random_ops.random_normal([3, 3], seed=42)
    rhs1 = random_ops.random_normal([3, 3], seed=42)
    rhs2 = random_ops.random_normal([3, 3], seed=42)
    with self.test_scope():
        s1 = linalg_ops.matrix_solve(lhs1, rhs1, adjoint=adjoint)
        s2 = linalg_ops.matrix_solve(lhs2, rhs2, adjoint=adjoint)
    self.assertAllEqual(*sess.run([s1, s2]))
