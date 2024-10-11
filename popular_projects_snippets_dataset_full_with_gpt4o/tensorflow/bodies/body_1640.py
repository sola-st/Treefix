# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_triangular_solve_op_test.py
clean_a = np.tril(a) if lower else np.triu(a)
with self.session() as sess:
    placeholder_a = MakePlaceholder(a, dtype)
    placeholder_ca = MakePlaceholder(clean_a, dtype)
    placeholder_b = MakePlaceholder(b, dtype)
    with self.test_scope():
        x = linalg_ops.matrix_triangular_solve(
            placeholder_a, placeholder_b, lower=lower, adjoint=adjoint)
    verification = test_util.matmul_without_tf32(
        placeholder_ca, x, adjoint_a=adjoint)
    self._VerifyTriangularSolveBase(sess, placeholder_a, placeholder_ca,
                                    placeholder_b, a, clean_a, b,
                                    verification, atol)
