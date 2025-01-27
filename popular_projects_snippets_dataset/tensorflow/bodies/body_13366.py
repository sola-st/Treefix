# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradients for the underdetermined case of MatrixSolveLs.

    This is the backprop for the solution to the normal equations of the second
    kind:
      X = F(A, B) = A * (A*A^T + lambda*I)^{-1} * B
    that (for lambda=0) solve the least squares problem
      min ||X||_F subject to A*X = B.
    """
a = op.inputs[0]
b = op.inputs[1]
l2_regularizer = math_ops.cast(op.inputs[2], a.dtype.base_dtype)
# pylint: disable=protected-access
chol = linalg_ops._RegularizedGramianCholesky(
    a, l2_regularizer=l2_regularizer, first_kind=False)
# pylint: enable=protected-access
grad_b = linalg_ops.cholesky_solve(chol, math_ops.matmul(a, grad))
# Temporary tmp = (A * A^T + lambda * I)^{-1} * B.
tmp = linalg_ops.cholesky_solve(chol, b)
a1 = math_ops.matmul(tmp, a, adjoint_a=True)
a1 = -math_ops.matmul(grad_b, a1)  # pylint: disable=invalid-unary-operand-type
a2 = grad - math_ops.matmul(a, grad_b, adjoint_a=True)
a2 = math_ops.matmul(tmp, a2, adjoint_b=True)
grad_a = a1 + a2
exit((grad_a, grad_b, None))
