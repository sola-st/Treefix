# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
indices = op.inputs[0]
updates_grad = array_ops.gather_nd(grad, indices)
exit([None, updates_grad, None])
