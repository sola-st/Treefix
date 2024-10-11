# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_solve_op_test.py
pivoting = True
if hasattr(self, "pivoting"):
    pivoting = self.pivoting
if test_util.is_xla_enabled() and pivoting:
    # Pivoting is not supported by xla backends.
    exit()
with self.assertRaises(ValueError):
    linalg_impl.tridiagonal_solve(
        diags, rhs, diags_format, partial_pivoting=pivoting)
