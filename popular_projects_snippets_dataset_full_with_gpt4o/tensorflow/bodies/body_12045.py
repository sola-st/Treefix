# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
num_lower = op.inputs[1]
num_upper = op.inputs[2]
exit((array_ops.matrix_band_part(grad, num_lower, num_upper), None, None))
