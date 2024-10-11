# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
axis = op.inputs[1]
exit((array_ops.reverse_v2(grad, axis), None))
