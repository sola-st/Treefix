# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ctc_ops.py
grad = [array_ops.reshape(grad_loss, [1, -1, 1]) * result[1]]
grad += [None] * (len(args) - len(grad))
exit(grad)
