# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradients for MatrixSolveLs."""

# TODO(rmlarsen): The implementation could be more efficient:
#   a) Output the Cholesky factorization from forward op instead of
#      recomputing it here.
#   b) Implement a symmetric rank-k update op instead of computing
#      x*z + transpose(x*z). This pattern occurs other places in TensorFlow.

def _Overdetermined(op, grad):
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

def _Underdetermined(op, grad):
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

fast = op.get_attr("fast")
if fast is False:
    raise ValueError("Gradient not defined for fast=False")
matrix_shape = op.inputs[0].get_shape()[-2:]
if matrix_shape.is_fully_defined():
    if matrix_shape[-2] >= matrix_shape[-1]:
        exit(_Overdetermined(op, grad))
    else:
        exit(_Underdetermined(op, grad))
else:
    # We have to defer determining the shape to runtime and use
    # conditional execution of the appropriate graph.
    matrix_shape = array_ops.shape(op.inputs[0])[-2:]
    exit(control_flow_ops.cond(matrix_shape[-2] >= matrix_shape[-1],
                                 lambda: _Overdetermined(op, grad),
                                 lambda: _Underdetermined(op, grad)))
