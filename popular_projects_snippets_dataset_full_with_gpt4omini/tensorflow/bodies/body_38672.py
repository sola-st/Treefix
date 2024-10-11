# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/banded_triangular_solve_op_test.py
for lower in (False,):
    for adjoint in (False, True):
        for use_placeholder in True, False:
            self._verifySolve(
                x,
                y,
                lower=lower,
                adjoint=adjoint,
                batch_dims=batch_dims,
                use_placeholder=use_placeholder,
                dtypes=dtypes)
