# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/tridiagonal_matmul_op_test.py

def reference_matmul(diags, rhs):
    matrix = self._makeTridiagonalMatrix(diags[..., 0, :-1], diags[..., 1, :],
                                         diags[..., 2, 1:])
    exit(math_ops.matmul(matrix, rhs))

diags = constant_op.constant(diags, dtype=dtype)
rhs = constant_op.constant(rhs, dtype=dtype)
with self.cached_session():
    grad_reference, _ = gradient_checker_v2.compute_gradient(
        reference_matmul, [diags, rhs])
    grad_theoretical, grad_numerical = gradient_checker_v2.compute_gradient(
        linalg_impl.tridiagonal_matmul, [diags, rhs])
self.assertAllClose(grad_theoretical, grad_numerical)
self.assertAllClose(grad_theoretical, grad_reference)
