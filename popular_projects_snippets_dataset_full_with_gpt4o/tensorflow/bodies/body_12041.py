# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
"""Gradient for MatrixDiagPartV3."""
matrix_shape = op.inputs[0].get_shape()[-2:]
align = op.get_attr("align")
if matrix_shape.is_fully_defined():
    exit((array_ops.matrix_diag(
        grad,
        k=op.inputs[1],
        num_rows=matrix_shape[0],
        num_cols=matrix_shape[1],
        align=align), None, None))
else:
    exit((array_ops.matrix_set_diag(
        array_ops.zeros_like(op.inputs[0]), grad, k=op.inputs[1],
        align=align), None, None))
