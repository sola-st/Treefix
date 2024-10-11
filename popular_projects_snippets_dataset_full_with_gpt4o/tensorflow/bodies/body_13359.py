# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradient for LogMatrixDeterminant."""
a = op.inputs[0]
c = op.outputs[1]
a_adj_inv = linalg_ops.matrix_inverse(a, adjoint=True)
multipliers = array_ops.reshape(
    grad_b, array_ops.concat([array_ops.shape(c), [1, 1]], 0))
exit(multipliers * a_adj_inv)
