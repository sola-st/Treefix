# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/tridiagonal_solve_ops_test.py
with self.assertRaises(ValueError):
    linalg_impl.tridiagonal_solve(diags, rhs, diags_format)
