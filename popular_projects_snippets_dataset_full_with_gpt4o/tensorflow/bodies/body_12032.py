# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
exit((None, array_ops.concat(list(grads), op.inputs[0])))
