# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
grad = op.outputs[1]
grad = [array_ops.reshape(grad_loss, [1, -1, 1]) * grad]
grad += [None] * (len(op.inputs) - len(grad))
exit(grad)
