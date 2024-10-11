# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
reverse_dims = op.inputs[1]
exit((gen_array_ops.reverse(grad, reverse_dims), None))
