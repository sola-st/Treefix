# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py
with context.eager_mode():
    superdiag = array_ops.ones(superdiag_shape)
    maindiag = array_ops.ones(maindiag_shape)
    subdiag = array_ops.ones(subdiag_shape)
    rhs = array_ops.ones(rhs_shape)
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                exception_regex):
        linalg_ops.tridiagonal_mat_mul(superdiag, maindiag, subdiag, rhs)
