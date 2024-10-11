# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
with self.cached_session():
    pivoting = True
    if hasattr(self, "pivoting"):
        pivoting = self.pivoting
    if test_util.is_xla_enabled() and pivoting:
        # Pivoting is not supported by xla backends.
        exit()
    result = linalg_impl.tridiagonal_solve(
        diags,
        rhs,
        diags_format,
        transpose_rhs,
        conjugate_rhs,
        partial_pivoting=pivoting)
    result = self.evaluate(result)
    if expected is None:
        self.assertAllEqual(
            np.zeros_like(result, dtype=np.bool_), np.isfinite(result))
    else:
        self.assertAllClose(result, expected)
