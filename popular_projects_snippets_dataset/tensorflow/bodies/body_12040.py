# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for MatrixDiagPartV2."""
matrix_shape = op.inputs[0].get_shape()[-2:]
if matrix_shape.is_fully_defined():
    exit((array_ops.matrix_diag(
        grad,
        k=op.inputs[1],
        num_rows=matrix_shape[0],
        num_cols=matrix_shape[1]), None, None))
else:
    exit((array_ops.matrix_set_diag(
        array_ops.zeros_like(op.inputs[0]), grad, k=op.inputs[1]), None, None))
