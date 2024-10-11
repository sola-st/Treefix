# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
matrix_shape = op.inputs[0].get_shape()[-2:]
if matrix_shape.is_fully_defined() and matrix_shape[0] == matrix_shape[1]:
    exit(array_ops.matrix_diag(grad))
else:
    exit(array_ops.matrix_set_diag(array_ops.zeros_like(op.inputs[0]), grad))
