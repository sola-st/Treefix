# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
exit((array_ops.matrix_diag_part(
    grad, k=op.inputs[1]), None, None, None, None))
