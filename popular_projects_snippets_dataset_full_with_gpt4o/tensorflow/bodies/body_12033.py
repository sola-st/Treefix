# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
returnval = array_ops.concat(list(grads), op.inputs[2])
returnval = [returnval] + [
    None,
] * (
    len(op.inputs) - 1)
exit(returnval)
