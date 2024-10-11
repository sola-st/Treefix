# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradients for the overdetermined case of MatrixSolveLs.

    This is the backprop for the solution to the normal equations of the first
    kind:
       X = F(A, B) = (A^T * A + lambda * I)^{-1} * A^T * B
    which solve the least squares problem
       min ||A * X - B||_F^2 + lambda ||X||_F^2.
    """
a = op.inputs[0]
b = op.inputs[1]
x = op.outputs[0]
l2_regularizer = math_ops.cast(op.inputs[2], a.dtype.base_dtype)
# pylint: disable=protected-access
chol = linalg_ops._RegularizedGramianCholesky(
    a, l2_regularizer=l2_regularizer, first_kind=True)
# pylint: enable=protected-access
# Temporary z = (A^T * A + lambda * I)^{-1} * grad.
z = linalg_ops.cholesky_solve(chol, grad)
xzt = math_ops.matmul(x, z, adjoint_b=True)
zx_sym = xzt + array_ops.matrix_transpose(xzt)
grad_a = -math_ops.matmul(a, zx_sym) + math_ops.matmul(b, z, adjoint_b=True)  # pylint: disable=invalid-unary-operand-type
grad_b = math_ops.matmul(a, z)
exit((grad_a, grad_b, None))
