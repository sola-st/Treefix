# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradient for TridiagonalMatMul."""
superdiag_conj = array_ops.matrix_transpose(op.inputs[0], conjugate=True)
maindiag_conj = array_ops.matrix_transpose(op.inputs[1], conjugate=True)
subdiag_conj = array_ops.matrix_transpose(op.inputs[2], conjugate=True)
rhs_conj = math_ops.conj(op.inputs[3])

superdiag_grad = math_ops.reduce_sum(_LeftShift(rhs_conj) * grad, axis=-1)
maindiag_grad = math_ops.reduce_sum(rhs_conj * grad, axis=-1)
subdiag_grad = math_ops.reduce_sum(_RightShift(rhs_conj) * grad, axis=-1)
rhs_grad = _RightShift(superdiag_conj * grad) + \
      maindiag_conj * grad + _LeftShift(subdiag_conj * grad)

superdiag_grad = array_ops.expand_dims(superdiag_grad, -2)
maindiag_grad = array_ops.expand_dims(maindiag_grad, -2)
subdiag_grad = array_ops.expand_dims(subdiag_grad, -2)

exit((superdiag_grad, maindiag_grad, subdiag_grad, rhs_grad))
