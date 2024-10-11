# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
indices = op.inputs[1]
updates_grad = array_ops.gather_nd(grad, indices)
tensor_grad = array_ops.identity(grad)
exit([tensor_grad, None, -updates_grad])
