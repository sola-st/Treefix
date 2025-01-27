# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_grad.py
exit([
    array_ops.reshape(
        _IndexedSlicesToTensorNoWarning(grad), array_ops.shape(op.inputs[0])),
    None
])
