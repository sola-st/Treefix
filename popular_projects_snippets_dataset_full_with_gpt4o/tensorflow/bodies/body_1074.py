# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
with self.session() as sess, self.test_scope():
    self.assertAllClose(
        sess.run(
            linalg_impl.tridiagonal_solve(
                _tfconst(diags),
                _tfconst(rhs),
                diags_format,
                transpose_rhs,
                conjugate_rhs=False,
                partial_pivoting=False)),
        np.asarray(expected, dtype=np.float32))
